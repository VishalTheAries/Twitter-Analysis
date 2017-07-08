from mongoengine import *
from config import *

connect(PROJECT_NAME,host=MONGO_HOST)

class Tweet(Document):
    content = StringField(required=True)
    date = DateTimeField(required=True)

    meta = {'indexes': [
        {'fields': ["$content"],
         'default_language': 'english'
        }
    ]}
