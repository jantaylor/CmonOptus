import pyspeedtest
import tweepy
import time

def sendTweet(ping, upload, download):
    auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
    auth.set_access_token('access_key', 'access_secret')

    api = tweepy.API(auth)

    api.update_status('@Optus, Why is my download only ' + str(round(download, 2)) + ', and upload only ' + str(round(upload, 2)) + '?')

if __name__ == "__main__":
    while True:
        st = pyspeedtest.SpeedTest()
        st.chooseserver()
        ping = st.ping()
        upload = st.upload()
        upload = upload/1000/1000
        download = st.download()
        download = download/1000/1000
        if (download < 75):
            print('Sending tweet...')
            sendTweet(ping, upload, download)
            time.sleep(7200)
