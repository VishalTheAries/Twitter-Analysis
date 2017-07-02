from flask import Flask,render_template,request

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

from models import *

app = Flask(__name__)



@app.route('/')    
def home_page():
    return render_template('index.html')

@app.route('/search',methods=['POST'])
def search():
    data = request.form.get('search_key','')
    objects = Tweet.objects.search_text(data).order_by('-date').all()
    # print len(objects)
    return render_template('search_results.html',results=objects)


if __name__ == "__main__":
    app.run() 