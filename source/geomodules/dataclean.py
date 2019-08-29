from pandas.io.json import json_normalize
import pandas as pd
import numpy as np
import requests


#Merge deadpool related columns into 1 and fill blanks with NaN values.
def deadpooled_finder(df):
    df['deadpooled'] = df[df.columns[10:13]].apply(lambda x: ','.join(x.dropna().astype(str)),
                                                                           axis=1).replace(r'^\s*$', np.nan, regex=True)
    return pd.concat([df, df['deadpooled']])


#Select alive companies. If they have 'deadpoled' data I understand they are dead.
def alives_finder(df):
    return df[pd.isnull(df['deadpooled'])]


# Dropping columns we no longer need.
def columns_drop(df, col):
    return df[[x for x in df.columns if x != col]]

def relevant_columns(df):
    return pd.DataFrame(df[['name', 'category_code', 'number_of_employees', 'offices', 'total_money_raised']])

def currency_converter(df):
    currency_type = {'C$': 'CAD',
                     '$': 'USD',
                     '€': 'EUR',
                     '£': 'GBP',
                     '¥': 'JPY',
                     'kr': 'SEK'}
    for symb, name in currency_type.items():
        if symb in df:
            return name

#Deleting currency symbols.
def symbol_deleter(df):
    currency_type = {'C$': 'CAD',
                '$': 'USD',
                '€': 'EUR',
                '£': 'GBP',
                '¥': 'JPY',
                'kr': 'SEK'}
    for symb, name in currency_type.items():
        if symb in df:
            return df.replace(symb, "")


#Converting "total_money_raised" into integers.
def money_converter(df):
    amount_type = dict(k='E3', M='E6', B='E9')
    return pd.to_numeric(df.replace(amount_type, regex=True)).astype(float)


#Create a dictionary with the needed exchange rates using an API to obtain real data.
def api_rates(url, df):
    response = requests.get(url)
    api_data = response.json()
    api_dataframe = pd.DataFrame(json_normalize(api_data))
    api_dict = {
            'CAD':api_dataframe['rates.CAD'][0],
            'EUR':api_dataframe['rates.EUR'][0],
            'GBP':api_dataframe['rates.GBP'][0],
            'JPY':api_dataframe['rates.JPY'][0],
            'SEK':api_dataframe['rates.SEK'][0],
            'USD':1
            }
    return pd.to_numeric(df.replace(api_dict, regex=True))


#Standarize all valuations into one currency ($) and convert them into millions.
def currency_normalizator(df):
    return ((df['amount_raised']/df['currency'])/1000).round(2)


def dropnulls(df):
    return df[pd.notnull(df['name'])]


#There are some companies which have >1 offices. Separate them into different rows.
def office_splitter(df):
    office_split = pd.DataFrame(df['offices'].tolist()).stack().reset_index(level=1, drop=True).rename('office')
    return df.merge(office_split, left_index=True, right_index=True).reset_index()

# Deleting duplicates
def duplicates_remover(df):
    df['duplicates'] = df['office'].astype(str)
    return df.drop_duplicates('duplicates', keep = 'first')


#I assume companies who have raised more money will pay higher income to their employees. But do not forget the number of employees is important.
def wealthy(df):
    wealth = pd.DataFrame((np.log(df['amount_raised_k$']).astype(str).replace('-inf','1').astype(float)*df['number_of_employees']))
    divisor = wealth.max()
    return wealth/divisor


#Detect special type of companies which might be interesting for some purpose. i.e.:news agencies (check readme)
def hot_encoder(df, category):
    lst = []
    for i in df:
        if i == category:
            lst.append(1)
        else:
            lst.append(0)
    return lst


#Function to convert the info within offices into a geopoint.
def geopoint(data):
    data = data['office']
    principal = None
    if data['latitude'] and data['longitude']:                   #Makes sure there is data
        principal = {
            "type":"Point",
            "coordinates":[data['longitude'], data['latitude']]
        }

    return {
        "lat": data['latitude'],
        "lng": data['longitude'],
        "geopoint": principal
    }

#Concatenating data with geopoints
def concatenator(df1, df2):
    return pd.concat([df1, df2], axis=1)


#Creating a json with the new dataframe to apply the geoindex using mongodb compass
def json_creator(df, name):
    return df.to_json(f'../data/{name}.json', orient="records")

