from .geoacquisition import *
from .geoclean import *
from .dataclean import columns_drop
from .geoapi import *




def read_geofile(host):
    print('Connecting to the database...')
    geodatabase = geomongo_connect(host)
    print('Looking for nearby companies...')
    geodatabase['offices_near'] = nearComps(host, geodatabase['geopoint'], rad_max_meters=1000)
    print('Looking for news agencies around....')
    geodatabase['news_agencies'] = nearNews(host, geodatabase['geopoint'], rad_max_meters=1000)
    return geodatabase


def geordering500(df):
    print("Normalizing column 'offices_near'...")
    df['offices_near'] = normalizator(df['offices_near'])
    print("Normalizing column news_agencies and weighting it negatively...")
    df['news_agencies'] = normalizator(df['news_agencies'])*(-0.1)
    print("Scoring...")
    df['final_score'] = final_score(df, 'wealth', 'news_agencies', 'offices_near')
    print('Selecting top 500...')
    top500 = top_500(df, 500)
    print('Dropping columns we no longer need...')
    top500 = columns_drop(top500, 'index')
    top500 = columns_drop(top500, '_id')
    return top500

def geoapi(top500):
    print('Looking for other bars...')
    top500['bar']=near_API(BASE_URL, top500,'bar', 1000)
    print('Looking for bus stops...')
    top500['bus']=near_API(BASE_URL, top500,'bus_station', 500)
    print('Looking for metro stations...')
    top500['subway_station']=near_API(BASE_URL, top500,'subway_station', 1000)
    print('Creating a csv file to avoid using the API again...')
    geotop500 = csv_creator(top500, 'top500')
    return geotop500

def geonormalizing(path):
    df = csv_reader(path)
    df['bar'] = normalizator(df['bar']) * (-0.2)
    df['bus'] = normalizator(df['bus']) * (0.5)
    df['subway_station'] = normalizator(df['subway_station']) * (0.5)
    print('Finding startups with no nearby bus/metro station and negatively weighting...')
    df['bus'] = no_transport(df['bus'])
    df['subway_station'] = no_transport(df['subway_station'])
    print('Obtaining final score and sorting...')
    df['score'] = final_score(df, 'bar', 'bus', 'subway_station')
    df['score'] = df[['score', 'final_score']].sum(axis = 1).round(2)
    df = columns_drop(df, 'index')
    print('Top10 startups to locate near around. Check these coordenates:')
    top10 = df.sort_values('score', ascending=False).reset_index().head(10)
    print(top10)
    return mapa(top10)



# a = read_geofile('mongodb://localhost:27017/')
# b = geordering500(a)
# c = geoapi(b)
# d = geonormalizing('../data/top500.csv', )
