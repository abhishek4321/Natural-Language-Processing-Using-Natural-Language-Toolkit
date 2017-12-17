#import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
#import MySQLdb
#import time
import json
#import db as t

#consumer key, consumer secret, access token, access secret.
ckey="K84aBjuLivUsCpYrOGlE9tmTj"
csecret="ehwia3OTpLL2lRXHtc246OJHXW1TvotxJKtjMvi3rjy0lAHyGn"
atoken="818098577616596992-DOPkac5Rt8wUPMlg8f4Xr1DvN5ikxMm"
asecret="jVblwuJR5GIgdZycofOTR0tsjTzabVBVplEvwC9dXVwHw"

#from temp import *

class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"]
        #sentiment_value,confidence-s.sentiment(tweet)

        print(tweet)
        #time.sleep(0.3)
        
        return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["yogi"])