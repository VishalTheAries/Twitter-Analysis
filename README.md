# Twitter Data Fetch 
Application runs on port 5000, change port in `app.py` by specifying the argument to `app.run(port=XXXX)`

Enter credential to Twitter API and MongoDb host inn `config.py`
run this application using following command
    `python app.py`
    then access your localhost by typing `localhost:5000` or `localhost:XXXX`
    
and to build the database first using twitter streaming api type following command
	`python task.py`

## About the Application:

### Features:

**1.** Fetch Tweets from twitter containing words specified in config.py.<br/>
**2.** Store Fetched Tweets into MongoDb Databse.<br/>
**3.** Full text search on the stored tweets.<br/>
**4.** Gives Insight about the stored tweets.<br/>

## Here is what this little application demonstrates:

1. Integration with the Twitter Streaming API: OAuth2.
2. Storing and Accessing MongoDB using ORM: mongoengine
3. Writing Mongo Aggregation Queries and indexing for full text search.
4. Plotting Graphs to give insight about data.


### [App Link*](http://twitter-data-fetch.herokuapp.com/)  
###### *Application is demostated with very basic GUI
