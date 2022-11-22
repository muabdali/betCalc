
import requests
import bs4
import time
import pandas as pd


def updateCSV():
    groupNameList = ['A','B','C','D','E','F','G','H','I']
    listCount = 0
    groupName = 'A'
    url = f"https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_{groupName}"



    while groupName != 'I':
        url = f"https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_{groupName}"
        r = requests.get(url)
        df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
        df = df_list[0] # returns the first 5 rows of the dataframe
        df.head()
        print(df)
        df.to_csv(f'Group{groupName}.csv')
        listCount = listCount + 1
        groupName = groupNameList[listCount]


