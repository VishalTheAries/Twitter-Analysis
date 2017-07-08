from __future__ import absolute_import

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
from dateutil import parser
from config import *
from models import *


class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        try:
            decoded = json.loads(data)
            date_tweet,text = '',''
            if decoded['created_at']:
                date_tweet = parser.parse(decoded['created_at'])
            if decoded['text']:
                text = decoded['text']
        except:
            pass
        if date_tweet and text:
            Tweet(content=text,date=date_tweet).save()
        return True

    def on_error(self, status):
        pass

if __name__ == '__main__':
    Tweet.drop_collection()
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=keywords)