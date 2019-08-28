from Pipelines.acquisition import *
from Pipelines.dataclean import *

def read_file(host):
    print('Reading file...')
    database = mongo_connect(host)
    database = mongo_query(database, 10, 51)
    return database

def cleaning(df):
    print('Cleaning and preparing your json...')
    dataframe = deadpooled_finder(df)
    dataframe = alives_finder(dataframe)
    dataframe = relevant_columns(dataframe)
    dataframe['currency'] = df['total_money_raised'].apply(currency_converter)
    dataframe['total_money_raised'] = df['total_money_raised'].apply(symbol_deleter)
    # dataframe = symbol_deleter(dataframe)
    dataframe['amount_raised'] = money_converter(dataframe['total_money_raised'])

    dataframe = api_rates(url)


    # dataframe = currency_rate(df)
    # dataframe = normalizator(df)
    # dataframe = office_splitter(df)
    # dataframe = duplicates_remover(df)
    # dataframe = wealthy(df)
    # dataframe = hot_encoder(df, category)
    # geonew = geopoint(dataframe)
    # dataframe = concatenator(dataframe, df2)
    # dataframe = json_creator(dataframe, name)
    return dataframe





#
# def deadpooled_finder(df):
#     df['deadpooled'] = df[df.columns[10:13]].apply(lambda x: ','.join(x.dropna().astype(str)),
#                                                                            axis=1).replace(r'^\s*$', np.nan, regex=True)
#     return df['deadpooled']

#one_office['deadpooled'] = deadpooled_finder(one_office)

a = read_file('mongodb://localhost:27017/')
b = cleaning(a)

# print(b.isnull().sum())
# print(len(b))
# print(b['currency'].unique())

print(b)
# print(b['currency'])

# print(b['total_money_raised'])
