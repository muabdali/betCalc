
import requests
import bs4
import time
import pandas as pd
import csv

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



"""
def deleteUseless():
    csv_file = f'Group{groupName}.csv'
    file = open(csv_file)
    csvreader = csv.reader(file)


    next(csvreader)

    rows = []
    for row in csvreader:
        rows.append(row)
    
    file.close

    with open(csv_file, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
"""

"""
def dbDeleteUseless():
    df = pd.read_csv(f'Group{groupName}.csv')
    df.drop(index=3,inplace=True)
    df.drop(index=2,inplace=True)
    print(df)

"""
updateCSV()
# reset variables
groupName = groupNameList[0]
listCount = 0