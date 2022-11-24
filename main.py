
import requests
import bs4
import time
import pandas as pd
import csv
import os
import shutil

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


def moveFile():
    groupManeList = ['A','B','C','D','E','F','G','H','I']
    groupMane = 'A'
    listCountt = 0
    while groupMane != 'I':
        os.rename(f"D:\betCalc-2\Group{groupMane}", f"D:\betCalc-2\Groups\Group{groupMane}")
        listCountt = listCountt + 1
        groupMane = groupManeList[listCount]


"""
def deleteUseless():
    groupNameLists = ['A','B','C','D','E','F','G','H','I']
    groupNames = 'A'
    listcounts = 0
    while listcounts != 8:
        csv_file = f'Group{groupNames}.csv'
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


        listcounts = listcounts + 1
        groupNames = groupNameLists[listCount]

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
groupName = 'A'
listCount = 0

import csv
import glob

#creates combined standings
def combinedStandings():
    csv_files = {}      # (header as tuple) : csv.writer()
    header_type_count = 1
    for filename in glob.glob('*.csv'):
        with open(filename, newline='') as f_input:
            csv_input = csv.reader(f_input)
            header = tuple(next(csv_input))
            
            try:
                csv_files[header].writerows(csv_input)
            except KeyError:
                f_output = open(f'combinedStandings{header_type_count:02}.csv', 'w', newline='')
                header_type_count += 1
                csv_output = csv.writer(f_output)
                csv_files[header] = csv_output
                csv_output.writerow(header)
                csv_output.writerows(csv_input)




def findPointAny():
    pointTotal = 0
    teamName = "Netherlands"
    with open('combinedStandings01.csv', 'rt') as f:
     reader = csv.reader(f, delimiter=',')
     for row in reader:
          if teamName == row[2]: # if the username shall be on column 3 (-> index 2)
              print ("is in file")


#combinedStandings()
findPointAny()
moveFile()

