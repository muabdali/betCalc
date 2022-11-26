import requests
import bs4
import time
import pandas as pd
import csv
from Functions.combinedStanding import combinedStandings


musTeam = ["Netherlands","Senegal","England","Wales","Argentina","Mexico","France","Australia","Germany","Spain","Belgium","Canada","Brazil","Cameroon","Portugal","Uruguay"]
aliTeam = ["Netherlands","Ecuador","Wales","England","Argentina","Saudi Arabia","Denmark","France","Germany","Spain","Belgium","Canada","Brazil","Serbia","Ghana","Portugal"]
shuaybTeam = ["Netherlands","Ecuador","England","Wales","Argentina","Poland","Australia","Denmark","Germany","Spain","Croatia","Belgium","Brazil","Serbia","Portugal","Uruguay"]
maxemTeam = ["Netherlands","Senegal","England","Wales","Argentina","Mexico","Denmark","Tunisia","Germany","Spain","Belgium","Canada","Brazil","Switzerland","Portugal","Uruguay"]



def updateCSV():
    global groupName 
    global groupNameList 
    global listCount
    groupNameList = ['A','B','C','D','E','F','G','H','I']
    listCount = 0
    groupName = 'A'
    url = f"https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_{groupName}"

    while groupName != 'I':
        url = f"https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_Group_{groupName}"
        r = requests.get(url)
        df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
        df = df_list[1] # returns the first 5 rows of the dataframe
        df.head()
        df.drop(index=3,inplace=True)
        df.drop(index=2,inplace=True)
        print(df)
        df.to_csv(f'Group{groupName}.csv')
        listCount = listCount + 1
        groupName = groupNameList[listCount]


updateCSV()


# reset variables
groupName = 'A'
listCount = 0

#findPointAny(musTeam)
combinedStandings()
#moveFile()