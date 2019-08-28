import requests as req
from dotenv import load_dotenv
import os
import pandas as pd

#Function to query Google's API and find info about other bars, bus and metro stations.

load_dotenv()

if not 'KEY' in os.environ:
    raise ValueError('This function requires a Google KEY in orer to work.')

API_KEY = os.environ["KEY"]
BASE_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch'

def near_API(BASE_URL, df, obj, rad):
    lst=[]
    for i in range(len(df)):
        lat=df['lat'][i]
        lng=df['lng'][i]
        res = req.get('{}/json?location={},{}&radius={}&type={}&key={}'.format(BASE_URL,lat,lng,rad,obj,API_KEY))
#         https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=1500&type=restaurant&keyword=cruise&key=YOUR_API_KEY
        near=res.json()
#         print(near)
        if near['status']=='OK':
            lst.append(len(near['results']))
        else:
            lst.append(0)
    return lst

# top500['bar']=near_API(BASE_URL, top500,'bar', 1000)
# top500['bus']=near_API(BASE_URL, top500,'bus_station', 500)
# top500['subway_station']=near_API(BASE_URL, top500,'subway_station', 1000)



# Saving the dataframe into a csv to avoid using the API again
def csv_creator(df, name):
     return df.to_csv(f'../data/{name}.csv', index=False)
# csv_creator(top500, 'top500')
# Importing the csv

def csv_reader(path):
    return pd.read_csv(path)
# df = csv_reader('../data/top500.csv')

#Normalizing competition, bus and subway.
# df['bar'] = normalizator(df['bar'])*(-0.2)
# df['bus'] = normalizator(df['bus'])*(0.5)
# df['subway_station'] = normalizator(df['subway_station'])*(0.5)

# Affecting very negatively if there is no transport availability.

def no_transport(df):
    lst = []
    for i in df:
        if i < 0.000000000000001:
            lst.append(-0.5)
        else:
            lst.append(i)
    return lst

# df['bus'] = no_transport(df['bus'])
# df['subway_station'] = no_transport(df['subway_station'])

#Obtaining final score

# df['score'] = final_score(df, 'bar', 'bus', 'subway_station')
# df['score'] = df[['score', 'final_score']].sum(axis = 1).round(2)

# df_final = df_final.sort_values('score', ascending = False)

