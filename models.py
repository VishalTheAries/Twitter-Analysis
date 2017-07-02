# print 'in model'
from mongoengine import *

MONGO_HOST = 'localhost'
# MONGO_PORT = 543264
PROJECT_NAME = 'twitterdata'

# print 'before connect'
connect(host='mongodb:'+PROJECT_NAME+'//ds145892.mlab.com:45892/heroku_00mz69jn')#, host=MONGO_HOST, port=MONGO_PORT)
# print 'out of connect'

class Tweet(Document):
    content = StringField(required=True)
    date = DateTimeField(required=True)

    meta = {'indexes': [
        {'fields': ["$content"],
         'default_language': 'english'
        }
    ]}
