def pipeline_queries():
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
            "_id": "$dayOfMonth", 
            "sum": { "$sum": 1 }
        }}
    ]
    pipeline_seconds = [
        { "$project": {
            "nominal": 1, 
            "second": { "$second": "$date" }
        }}, 
        { "$group": {
            "_id": "$second", 
            "sum": { "$sum": 1 }
        }}
    ]

    pipeline_hour = [
        { "$project": {
            "nominal": 1, 
            "minute": { "$minute": "$date" }
        }}, 
        { "$group": {
            "_id": "$minute", 
            "sum": { "$sum": 1 }
        }}
    ]

    return pipeline_monthly,pipeline_weekly,pipeline_daily,pipeline_seconds,pipeline_hour