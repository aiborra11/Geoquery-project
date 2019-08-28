from pymongo import MongoClient
import pandas as pd

#Connecting the database with the queried data (companies_cb)
def mongo_connect(host):
    client = MongoClient(host)
    db = client.DBcompanies_cb
    data = db.companies_cb
    return data


# Query using Pymongo to receive all the required data for my analysis. (I know we should query everything at the same place (pymongo or mongodb compass), but was interested in trying both to learn.).
def mongo_query(data, min_employee=10, max_employee=51):
    one_office = data.find({'$and': [
        {'offices': {'$exists': True}},
        {'offices': {'$ne': None}},
        {'number_of_employees': {'$gte': min_employee}},
        {'number_of_employees': {'$lte': max_employee}},
        {'offices.latitude': {'$ne': None}},
        {'offices.longitude': {'$ne': None}},
        {'offices.latitude': {'$exists': True}},
        {'offices.longitude': {'$exists': True}}

    ]})

    return pd.DataFrame(one_office)


