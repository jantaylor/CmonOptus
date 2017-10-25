import pyspeedtest
import tweepy
import time
import datetime

from datetime import date
from random import randint

auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_key', 'access_secret')
lastPassed = datetime.datetime.now()

def sendTweet(ping, upload, download):
    api = tweepy.API(auth)

    if download < 75:
        print('Sending negative tweet...')
        api.update_status('.@Optus, Why am I getting ' + str(round(download, 2)) + 'down/' + str(round(upload, 2)) + 'up, when I pay for 100down/40up in Wollongong, NSW? #NBN #Australia #Optus #Broadband')
    else:
        print('Sending positive tweet')
        api.update_status('.@Optus, congrats on having >75 download for the first time since' + str(lastPassed.day) + '/' + str(lastPassed.month) + '/' + str(lastPassed.year))
        lastPassed = datetime.datetime.now()

def sleep(sleeptime):
    m, s = divmod(sleeptime, 60)
    h, m = divmod(m, 60)
    print("Checking speeds again in: %d hours %02d minutes and %02d seconds.\n"%(h,m,s))
    time.sleep(sleeptime)

if __name__ == "__main__":
    while True:
        st = pyspeedtest.SpeedTest()
        st.chooseserver()
        sendTweet(st.ping(), st.upload()/1000/1000, st.download()/1000/1000)
        sleep(randint(3000, 6000))
