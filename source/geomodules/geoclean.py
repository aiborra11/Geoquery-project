
#Normalizing near offices and near news_agencies (I weighted it to a 10% value)
def normalizator (df):
    return df/df.max()

#Summing up wealth, news_agencies and offices_near to obtain a final score.
def final_score(df, col1, col2, col3):
    return df[[col1, col2, col3]].sum(axis = 1)

#Select top 500 to test the api query. Then if it is not very expensive, we will try with the whole dataset.
def top_500(df, num):
    return df.sort_values('final_score', ascending = False).reset_index().head(num)

