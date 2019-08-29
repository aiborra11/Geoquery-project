import requests as req
from dotenv import load_dotenv
import os
import pandas as pd
import folium
from folium.plugins import FastMarkerCluster
import webbrowser

#Function to query Google's API and find info about other bars, bus and metro stations.

load_dotenv()

if not 'KEY' in os.environ:
    raise ValueError('This function requires a Google KEY in orer to work.')

API_KEY = os.environ["KEY"]
BASE_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch'

def near_API(BASE_URL, df, obj, rad):
    lst=[]
    for i in range(len(df)):
        lat = df['lat'][i]
        lng = df['lng'][i]
        res = req.get('{}/json?location={},{}&radius={}&type={}&key={}'.format(BASE_URL,lat,lng,rad,obj,API_KEY))
        near = res.json()
        if near['status'] == 'OK':
            lst.append(len(near['results']))
        else:
            lst.append(0)
    return lst


# Saving the dataframe into a csv to avoid using the API again
def csv_creator(df, name):
     return df.to_csv(f'../data/{name}.csv', index=False)


def csv_reader(path):
    return pd.read_csv(path)

def no_transport(df):
    lst = []
    for i in df:
        if i < 0.000000000000001:
            lst.append(-0.5)
        else:
            lst.append(i)
    return lst


def mapa(df):
    latlng = df[['lat', 'lng']]
    mi = folium.Map(zoom_start=15)
    minimap = FastMarkerCluster(latlng).add_to(mi)
    mi.add_child(minimap)
    mi.save('../pdf/bar.html')
    return webbrowser.open('file://'+ os.path.realpath('../pdf/bar.html'))
