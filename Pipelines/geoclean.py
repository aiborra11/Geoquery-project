from Pipelines.Pipeline1ipeline1.geoacquisition import *

from pymongo import MongoClient
import pandas as pd
import pymongo
import numpy as np
import re
import requests as req
import json
from dotenv import load_dotenv
import os

#Normalizing near offices and near news_agencies (I weighted it to a 10% value)
def normalizator (df):
    return df/df.max()

# df_comp['offices_near'] = normalizator(df_comp['offices_near'])
# df_comp['news_agencies'] = normalizator(df_comp['news_agencies'])*(-0.1)

#Summing up wealth, news_agencies and offices_near to obtain a final score.
def final_score(df, col1, col2, col3):
    return df[[col1, col2, col3]].sum(axis = 1)

# df_comp['final_score'] = final_score(df_comp, 'wealth', 'news_agencies', 'offices_near')

