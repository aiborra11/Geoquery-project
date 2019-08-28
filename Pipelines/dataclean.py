# from Pipelines.Pipeline1.acquisition import *

from pandas.io.json import json_normalize
import pandas as pd
import numpy as np
import requests


#Merge deadpool related columns into 1 and fill blanks with NaN values.
def deadpooled_finder(df):
    df['deadpooled'] = df[df.columns[10:13]].apply(lambda x: ','.join(x.dropna().astype(str)),
                                                                           axis=1).replace(r'^\s*$', np.nan, regex=True)
    return pd.concat([df, df['deadpooled']])




#one_office['deadpooled'] = deadpooled_finder(one_office)

#Select alive companies. If they have 'deadpoled' data I understand they are dead.
def alives_finder(df):
    return df[pd.isnull(df['deadpooled'])]

#one_office = alives_finder(one_office)

# Dropping columns we no longer need.
def columns_drop(df, col):
    return df[[x for x in df.columns if x != col]]

def relevant_columns(df):
    return pd.DataFrame(df[['name', 'category_code', 'number_of_employees', 'offices', 'total_money_raised']])

#data = relevant_columns(one_office)


# Converting symbols into string values for future uses.
# def currency_converter(df):
#     currency_type = {'C$': 'CAD',
#                      '$': 'USD',
#                      '€': 'EUR',
#                      '£': 'GBP',
#                      '¥': 'JPY',
#                      'kr': 'SEK'}
#     print('s')
#     lst = []
#     for symb, name in currency_type.items():
#         if symb in df:
#             lst.append(name)
#
#     df['currency'] = pd.DataFrame(lst)
#     return pd.concat([df, df['currency']])





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

# data['currency'] = data['total_money_raised'].apply(currency_converter)

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

# data['total_money_raised'] = data['total_money_raised'].apply(symbol_deleter)

#Converting "total_money_raised" into integers.
def money_converter(df):
    amount_type = dict(k='E3', M='E6', B='E9')
    return pd.to_numeric(df.replace(amount_type, regex=True)).astype(float)

# data['amount_raised'] = money_converter(data['total_money_raised'])


# # Create a dictionary with the needed exchange rates using an API to obtain real data.
# def api_rates(url):
#     response = requests.get(url)
#     api_data = response.json()
#     api_dataframe = pd.DataFrame(json_normalize(api_data))
#     api_dict = {
#             'CAD':api_dataframe['rates.CAD'][0],
#             'EUR':api_dataframe['rates.EUR'][0],
#             'GBP':api_dataframe['rates.GBP'][0],
#             'JPY':api_dataframe['rates.JPY'][0],
#             'SEK':api_dataframe['rates.SEK'][0],
#             'USD':1
#             }
#     return api_dict
#
# api_dict = api_rates('https://api.exchangerate-api.com/v4/latest/USD')
#
# #Set the currency valuation for every company.
# def currency_rate(df, api_dict):
#     return pd.to_numeric(df.replace(api_dict, regex=True))
#
# # data['currency'] = currency_rate(data['currency'], api_dict)


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

# data['amount_raised_k$'] = normalizator(data)

def dropnulls(df):
    return df[pd.notnull(df['name'])]


#Dropping more columns

# data = columns_drop(data, 'total_money_raised')
# data = columns_drop(data, 'currency')
# data = columns_drop(data, 'amount_raised')

#There are some companies which have >1 offices. Separate them into different rows.

def office_splitter(df):
    office_split = pd.DataFrame(df['offices'].tolist()).stack().reset_index(level=1, drop=True).rename('office')
    return df.merge(office_split, left_index=True, right_index=True).reset_index()


# office_merged = office_splitter(data)

# office_merged = columns_drop(office_merged, 'offices')


# Deleting duplicates
def duplicates_remover(df):
    df['duplicates'] = df['office'].astype(str)
    return df.drop_duplicates('duplicates', keep = 'first')

# office_merged = duplicates_remover(office_merged)
# office_merged = columns_drop(office_merged, 'duplicates')


#I assume companies who have raised more money will pay higher income to their employees. But do not forget the number of employees is important.
def wealthy(df):
    wealth = pd.DataFrame((np.log(df['amount_raised_k$']).astype(str).replace('-inf','1').astype(float)*df['number_of_employees']))
    divisor = wealth.max()
    return wealth/divisor

# office_merged['wealth'] = wealthy(office_merged)

#Detect special type of companies which might be interesting for some purpose. i.e.:news agencies (check readme)
def hot_encoder(df, category):
    lst = []
    for i in df:
        if i == category:
            lst.append(1)
        else:
            lst.append(0)
    return lst

# office_merged['news_agencies'] = hot_encoder(office_merged['category_code'], 'news')


#Function to convert the info within offices into a geopoint.
def geopoint(data):
    data = data['office']
    principal = None
    if data['latitude'] and data['longitude']:                   #Make sure there is data
        principal = {
            "type":"Point",
            "coordinates":[data['longitude'], data['latitude']]
        }

    return {
        "lat": data['latitude'],
        "lng": data['longitude'],
        "geopoint": principal
    }

# geopoint = office_merged.apply(geopoint, result_type="expand", axis=1).dropna()

#Concatenating data with geopoints
def concatenator(df1, df2):
    return pd.concat([df1, df2], axis=1)

# offices_geo = concatenator(office_merged, geopoint)
#Dropping columns we no longer need
# offices_geo = columns_drop(offices_geo, 'office')
# offices_geo = columns_drop(offices_geo, 'index')

#Creating a json with the new dataframe to apply the geoindex using mongodb compass
def json_creator(df, name):
    return df.to_json(f'../data/{name}.json', orient="records")





# json_creator(offices_geo, 'geoffices')


# Create the new collection in mongodb compass (geo_offices in my case) and import the geoffices.json writting the following comand into the terminal:
# mongoimport --db DBcompanies_cb --collection companies_clean --file geoffices.json --jsonArray
# Now move into the indexes area inside mongodb compass and create an index selecting the 'geopoint' column and 2dsphere. The result should look like this:





#We might have problems with the index if we want to use pipelines. Try a python comand to create the 2dsphere index without using mongodb.



#2nd jupyter notebook.

