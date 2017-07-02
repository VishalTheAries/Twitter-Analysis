from __future__ import absolute_import

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from dateutil import parser

from models import *
# print 'model imported'

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="XorHCfXwlJI6lx4bVGxgkv7Qb"
consumer_secret="orNAnnTGxpJXTbir16yDMqNdxn7KoTShBXMW2gk14x2SN8vK7t"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="161152310-l3FOKvAvt0fqZuyV3QoWissZJFOzmhXhim0gWYtQ"
access_token_secret="Z93qMGc6gTdUsI7u0gjzsLnDY3E1VrjgIs09LR1RVatmk"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        try:
            # print 'data recieved'
            decoded = json.loads(data)
            # print data
            date_tweet,text = '',''
            if decoded['created_at']:
                date_tweet = parser.parse(decoded['created_at'])
            # print type(decoded['created_at'])
            if decoded['text']:
                text = decoded['text']
            print decoded['coordinates']
            # print date_tweet,text
        except:
            pass
        if date_tweet and text:
            Tweet(content=text,date=date_tweet).save()
            # print 'tweet stored'
        return True

    def on_error(self, status):
        # print(status)
        pass

if __name__ == '__main__':

    Tweet.drop_collection()
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    # print 'stream connected'
    stream.filter(track=['analytics'])