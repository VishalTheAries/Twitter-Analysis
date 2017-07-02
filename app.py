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

@app.route('/analytics')    
def analytics_page():
    pipeline_monthly = [
        { "$project": {
            "nominal": 1, 
            "month": { "$month": "$date" }
        }}, 
        { "$group": {
            "_id": "$month", 
            "sum": { "$sum": 1 }
        }}
    ]
    pipeline_weekly = [
        { 
            "$project": {
                "createdAtWeek": { "$week": "$date" },
                "createdAtMonth": { "$month": "$date" },
                "rating": 1
            }
        },
        {
             "$group": {
                 "_id": "$createdAtWeek",
                 "sum": { "$sum": 1 },
                 "month": { "$first": "$createdAtMonth" }
             }
        }
    ]
    pipeline_daily = [
        { "$project": {
            "nominal": 1, 
            "dayOfMonth": { "$dayOfMonth": "$date" }
        }}, 
        { "$group": {
            "_id": "$month", 
            "sum": { "$dayOfMonth": 1 }
        }}
    ]
    results_monthly,results_weekly,results_daily=[],[],[]
    # import pdb;pdb.set_trace()
    try:
        results_monthly = list(Tweet.objects.aggregate(*pipeline_monthly))
        results_weekly = list(Tweet.objects.aggregate(*pipeline_weekly))
        results_daily = list(Tweet.objects.aggregate(*pipeline_daily))
    except:
        pass
    return render_template('analytics.html',results_monthly=results_monthly,results_weekly=results_weekly)

if __name__ == "__main__":
    app.run() 


    # pipeline = [{
    #         "$project" : {
    #             "year" : {
    #                 "$year" : "$date"
    #             },
    #             "month" : {
    #                 "$month" : "$date"
    #             },
    #             "week" : {
    #                 "$week" : "$date"
    #             },
    #             "day" : {
    #                 "$dayOfWeek" : "$date"
    #             },
    #             "_id" : 1,
    #             "weight" : 1
    #         }
    #     }, {
    #         "$group" : {
    #             "_id" : {
    #                 "year" : "$year",
    #                 "month" : "$month",
    #                 "week" : "$week",
    #                 "day" : "$day"
    #             },
    #             "totalWeightDaily" : {
    #                 "$sum" : 1
    #             }
    #         }
    #     },
    #     {
    #         "$group" : {

    #             "_id" : {
    #                 "year" : "$_id.year",
    #                 "month" : "$_id.month",
    #                 "week" : "$_id.week"
    #             },
    #             "totalWeightWeekly" : {
    #                 "$sum" : "$totalWeightDaily"
    #             },
    #             "totalWeightDay" : {
    #                 "$push" : {
    #                     "totalWeightDay" : "$totalWeightDaily",
    #                     "dayOfWeek" : "$_id.day"
    #                 }
    #             }
    #         }
    #     }
    # ]