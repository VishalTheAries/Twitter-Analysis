from flask import Flask,render_template,request
import json
from models import *
from pipeline_queries import *

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
        
    pipeline_monthly,pipeline_weekly,pipeline_daily,pipeline_seconds,pipeline_hour = pipeline_queries()
    results_monthly,resucompliancelts_weekly,results_daily=[],[],[]
    results_second ,results_hour= [],[]
    # import pdb;pdb.set_trace()
    try:
        results_monthly = list(Tweet.objects.aggregate(*pipeline_monthly))
        results_weekly = list(Tweet.objects.aggregate(*pipeline_weekly))
        results_daily = list(Tweet.objects.aggregate(*pipeline_daily))
        results_second = list(Tweet.objects.aggregate(*pipeline_seconds))
        results_hour = list(Tweet.objects.aggregate(*pipeline_hour))
    except:
        pass
    
    results_second_list=[0]*60
    for data in results_second:
        results_second_list[data['_id']-1]=data['sum']

    results_hour_list=[0]*60
    for data in results_hour:
        results_hour_list[data['_id']-1]=data['sum']
    
    return render_template('analytics.html',
                                results_monthly=results_monthly,
                                results_weekly=results_weekly,
                                results_daily=results_daily,
                                results_second_list=results_second_list,
                                results_second=results_second,
                                results_hour_list=results_hour_list,
                                results_hour=results_hour)


if __name__ == "__main__":
    app.run() 
