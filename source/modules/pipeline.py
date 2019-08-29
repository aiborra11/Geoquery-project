from .acquisition import *
from .dataclean import *
# from .test import *


def read_file(host):
    print('Reading file...')
    database = mongo_connect(host)
    database = mongo_query(database, 10, 51)
    return database


def cleaning(df):
    print('Cleaning and preparing your json...')
    dataframe = deadpooled_finder(df)
    print('Dropping deadpooled companies...')
    dataframe = alives_finder(dataframe)
    dataframe = relevant_columns(dataframe)
    dataframe['currency'] = df['total_money_raised'].apply(currency_converter)
    dataframe['total_money_raised'] = df['total_money_raised'].apply(symbol_deleter)
    # dataframe = symbol_deleter(dataframe)
    print('Converting money raised into $...')
    dataframe['amount_raised'] = money_converter(dataframe['total_money_raised'])
    dataframe['currency'] = api_rates('https://api.exchangerate-api.com/v4/latest/USD', dataframe['currency'])
    # api_dict = api_rates('https://api.exchangerate-api.com/v4/latest/USD')
    # dataframe['currency'] = currency_rate(dataframe['currency'], api_dict)
    dataframe['amount_raised_k$'] = currency_normalizator(dataframe)
    print('Dropping columns...')
    dataframe = columns_drop(dataframe, 'total_money_raised')
    dataframe = columns_drop(dataframe, 'currency')
    dataframe = columns_drop(dataframe, 'amount_raised')
    dataframe = dropnulls(dataframe)
    dataframe = office_splitter(dataframe)
    dataframe = columns_drop(dataframe, 'offices')
    dataframe = duplicates_remover(dataframe)
    print('Measuring wealthy...')
    dataframe['wealthy'] = wealthy(dataframe)
    dataframe['news_agencies'] = hot_encoder(dataframe['category_code'], 'news')
    geonew = dataframe.apply(geopoint, result_type="expand", axis=1).dropna()
    dataframe = concatenator(dataframe, geonew)
    print('Dropping more columns...')
    dataframe = columns_drop(dataframe, 'index')
    dataframe = columns_drop(dataframe, 'office')
    dataframe = columns_drop(dataframe, 'duplicates')
    dataframe = json_creator(dataframe, 'geofficestesting')
    print('Next steps using MongoDB Compass: \n 1. Create a new collection (geo_offices in my case) to import the geoffices.json. \n 2. Write the following command into your terminal:\n   ** mongoimport --db DBcompanies_cb --collection companies_clean --file geoffices.json --jsonArray ** \n 3. Move into the indexes area inside Mongodb Compass and create an index selecting the "geopoint" column and setting 2dsphere.')
    return dataframe

# def pdfgenerator(df):
#     return PDFgenerator(df)


# a = read_file('mongodb://localhost:27017/')
# b = cleaning(a)

