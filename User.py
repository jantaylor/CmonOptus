# Big thanks to the following contributors!
#   sp0
#   gregsifr

import pyspeedtest
import tweepy
import time
import datetime
import yaml
import sys
import plotly.plotly as py
import plotly.graph_objs as go

from datetime import date
from random import randint

def readConfig(filepath='config.yaml'):
    with open(filepath, 'r') as f:
        details = yaml.load(f)
    return details

def tweepyAuthentication(details):
    auth = tweepy.OAuthHandler(details['consumer_key'], details['consumer_secret'])
    auth.set_access_token(details['access_key'], details['access_secret'])
    return auth

def collectConnectionStatistics():
    st = pyspeedtest.SpeedTest()
    st.chooseserver()
    return st.upload()/1000/1000, st.download()/1000/100

def sendTweet(upload, download, details, auth):
    api = tweepy.API(auth)

    print('Sending negative tweet...')
    api.update_status(status='.@Optus @NBN_Australia, Why am I getting ' + str(round(download, 1)) + 'down/' + str(round(upload, 1)) + 'up, when I pay for 100down/40up in Wollongong, NSW? #NBN #Australia #Optus')

def sleep(sleeptime):
    m, s = divmod(sleeptime, 60)
    h, m = divmod(m, 60)
    print("Checking speeds again in: %d hours %02d minutes and %02d seconds.\n"%(h,m,s))
    time.sleep(sleeptime)

if __name__ == "__main__":
    # Allow command line args
    if len(sys.argv) > 1:
        details = readConfig(sys.argv[1])
    else:
        details = readConfig()

    auth = tweepyAuthentication(details)

    while True:
        upload, download = collectConnectionStatistics()
        if download < details['paid_download_speed']*0.75:
            sendTweet(upload, download, details, auth)
        else:
            print('Surprisingly speed was good!')
        
        time.sleep(randint(details['check_interval']*0.75, details['check_interval']*1.25))