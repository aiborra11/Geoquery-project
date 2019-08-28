from pymongo import MongoClient
import pandas as pd

#Connecting the database with the geo_offices data and returning the dataframe.

def geomongo_connect(host):
    client = MongoClient(host)
    db = client.DBcompanies_cb
    data = db.companies_clean.find()
    return pd.DataFrame(data)


# df_comp = geomongo_connect('mongodb://localhost:27017/')

#Reordering the dataframe and dropping the column id
# def reorder(df):
#     return df[['name', 'lat', 'lng', 'geopoint', 'number_of_employees','amount_raised_k$','category_code', 'wealth', 'news_agencies']]

#data_comp = reorder(df_comp)


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

# df_comp['offices_near'] = nearComps('mongodb://localhost:27017/', df_comp['geopoint'])



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


# df_comp['news_agencies'] = nearNews('mongodb://localhost:27017/', df_comp["geopoint"])

