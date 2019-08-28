from pymongo import MongoClient
import pandas as pd

#Connecting the database with the geo_offices data and returning the dataframe.
def geomongo_connect(host):
    client = MongoClient(host)
    db = client.DBcompanies_cb
    data = db.companies_clean.find()
    return pd.DataFrame(data)


def nearComps(host, df, rad_max_meters=1000):
        client = MongoClient(host)
        db = client.DBcompanies_cb
        lst = []
        for i in range(len(df)):
            near = db.companies_clean.find({'$and': [{
                'geopoint': {
                    '$near': {
                        '$geometry': df[i],
                        '$maxDistance': rad_max_meters
                    }
                }
            }]})
            data = pd.DataFrame(near)
            lst.append(data.shape[0])
        return lst


# Querying near news_agencies
def nearNews(host, df, rad_max_meters=1000):
    client = MongoClient(host)
    db = client.DBcompanies_cb
    lst = []
    for i in range(len(df)):
        near = db.companies_clean.find({'$and': [{
            "geopoint": {
                "$near": {
                    "$geometry": df[i],
                    "$maxDistance": rad_max_meters
                }
            }}, {
            'news_agencies': 1
        }]})

        data = pd.DataFrame(near)
        lst.append(data.shape[0])
    return lst
