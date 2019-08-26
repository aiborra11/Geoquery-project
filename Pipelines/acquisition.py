from pymongo import MongoClient
import pandas as pd



#Connecting the database with the queried data (companies_cb)
def mongo_connect(host):             # mongodb://localhost:27017/
    client = MongoClient(host)
    db = client.DBcompanies_cb
    data = db.companies_cb
    return data
#data = mongo_connect('mongodb://localhost:27017/')


# Query using Pymongo to receive all the required data for my analysis. (I know we should query everything at the same place (pymongo or mongodb compass), but was interested in trying both to learn.).
def mongo_query(data, min_employee, max_employee):
    one_office =  data.find({'$and': [
        {'offices': {'$exists': True}},
        {'offices': {'$ne': None}},
        #     {'number_of_employees':{'$exists':True}}
        {'number_of_employees': {'$gte': min_employee}},        #10
        {'number_of_employees': {'$lte': max_employee}},        #51
        {'offices.latitude': {'$ne': None}},
        {'offices.longitude': {'$ne': None}},
        {'offices.latitude': {'$exists': True}},
        {'offices.longitude': {'$exists': True}}

    ]})

    return pd.DataFrame(one_office)

#one_office = mongo_query(data, 10, 51)

