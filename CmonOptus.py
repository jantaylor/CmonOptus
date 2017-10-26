import sys
import time
from datetime import date
from datetime import datetime
from random import randint

import pyspeedtest
import tweepy
import yaml
import plotly.plotly as py
import plotly.graph_objs as go


def readConfig(filepath='config.yaml'):
    with open(filepath, 'r') as f:
        details = yaml.load(f)
    return details

def tweepyAuthentication(details):
    auth = tweepy.OAuthHandler(details['consumer_key'], details['consumer_secret'])
    auth.set_access_token(details['access_token'], details['access_token_secret'])
    return auth

def collectConnectionStatistics():
    st = pyspeedtest.SpeedTest()
    st.chooseserver()
    return st.upload()/1000/1000, st.download()/1000/1000

def sendTweet(upload, download, details, auth):
    api = tweepy.API(auth)

    tweet = '%s, Why am I getting %.1fdown/%.1fup, when I pay for %ddown/%dup in %s? #%s'
    print(datetime.now().strftime("%x %X") + ": " + tweet % (details['service_provider'], download, upload, details['paid_download_speed'], details['paid_upload_speed'], details['location'], details['service_provider']))
    api.update_status(tweet % (details['service_provider'], download, upload, details['paid_download_speed'], details['paid_upload_speed'], details['location'], details['service_provider']))

def sleep(sleeptime):
    m, s = divmod(sleeptime, 60)
    h, m = divmod(m, 60)
    print("Checking speeds again in: %d hours %02d minutes and %02d seconds.\n"%(h,m,s))
    time.sleep(sleeptime)

def isTimedOut(timeout, previous_tweet_time):
    if previous_tweet_time is not None:
        time_diff = datetime.now() - previous_tweet_time
        if time_diff.days > 0 or time_diff.seconds > timeout:
            return True

    return False


if __name__ == "__main__":
    # Allow command line args
    if len(sys.argv) > 1:
        details = readConfig(sys.argv[1])
    else:
        details = readConfig()

    auth = tweepyAuthentication(details)

    previous_tweet_time = None

    while True:
        upload, download = collectConnectionStatistics()
        if not isTimedOut(details['timeout_interval'], previous_tweet_time):
            if download < int(details['paid_download_speed'])*0.5:
                previous_tweet_time = datetime.now()
                sendTweet(upload, download, details, auth)
            else:
                print('Surprisingly speed was good!')
        
        time.sleep(randint(int(details['check_interval'])*0.75, int(details['check_interval'])*1.25))