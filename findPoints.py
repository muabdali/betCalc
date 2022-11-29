import csv
import pandas as pd
from functools import reduce
from datetime import date

# teams
musTeam = ["Netherlands","Senegal","England","Wales","Argentina","Mexico","France","Australia","Germany","Spain","Belgium","Canada","Brazil","Cameroon","Portugal","Uruguay"]
aliTeam = ["Netherlands","Ecuador","Wales","England","Argentina","Saudi Arabia","Denmark","France","Germany","Spain","Belgium","Canada","Brazil","Serbia","Ghana","Portugal"]
shuaybTeam = ["Netherlands","Ecuador","England","Wales","Argentina","Poland","Australia","Denmark","Germany","Spain","Croatia","Belgium","Brazil","Serbia","Portugal","Uruguay"]
maxemTeam = ["Netherlands","Senegal","England","Wales","Argentina","Mexico","Denmark","Tunisia","Germany","Spain","Belgium","Canada","Brazil","Switzerland","Portugal","Uruguay"]

allTeams = [musTeam,aliTeam,shuaybTeam,maxemTeam]

col_names = ['team_names','t','tr','f','fi','s','se','e','n','ten']
df = pd.read_csv("combinedStandings01.csv", names=col_names, header=0)

names = df.team_names.to_list()
print(names)
# fix needed, remove all (A) from list values

def findPointdF(chosenTeam):
    global res
    global pointTotal
    pointTotal = 0
    countTotal = 0
    res = reduce(lambda x, y: x+chosenTeam.count(y), set(names), 0)
    print(str(res))



def findPerfects(chosenTeam):
    global pointFirstPerfectTotal
    pointFirstPerfectTotal = 0
    FirstTeams = df.iloc[::2]
    FirstListTeams = chosenTeam[::2]
    for country in FirstListTeams:
        if country in FirstTeams.values:
            pointFirstPerfectTotal = pointFirstPerfectTotal + 1
    print(pointFirstPerfectTotal)
    FirstTeams.to_csv('First2ptstandings.csv')
    return pointFirstPerfectTotal



def findSecondPerfects(chosenTeam):
    global pointSecondPerfectTotal
    pointSecondPerfectTotal = 0
    dfSecond_2 = pd.read_csv("combinedStandings01.csv")
    SecondTeams = dfSecond_2.iloc[1::2]
    SecondTeams.to_csv("Second2PtsStandings.csv")
    SecondListTeams = chosenTeam[1::2]
    for country in SecondListTeams:
        if country in SecondTeams.values:
            pointSecondPerfectTotal = pointSecondPerfectTotal + 1
    print(pointSecondPerfectTotal)
    return pointSecondPerfectTotal


def findAllPoints(FUNCTIONCHOSEN):
    findPointdF(chosenTeam=FUNCTIONCHOSEN)
    findPerfects(chosenTeam=FUNCTIONCHOSEN)
    findSecondPerfects(chosenTeam=FUNCTIONCHOSEN)

# very janky, coudlve done dictionary but too lazy
def pointsPerTeam():
    one = 'musTeam'
    two = 'aliTeam'
    three = 'shuaybTeam'
    four = 'maxemTeam'
    pointCounter = 0
    for team in allTeams:
        findAllPoints(team)
        allTotals = res + pointFirstPerfectTotal + pointSecondPerfectTotal
        pointCounter = pointCounter + 1
        if pointCounter == 1:
            print(f'{one} - {allTotals}')
            updateHistory(one, allTotals)
        elif pointCounter == 2:
            print(f'{two} - {allTotals}')
            updateHistory(two, allTotals)
        elif pointCounter == 3:
            print(f'{three} - {allTotals}')  
            updateHistory(three, allTotals)          
        elif pointCounter == 4:
            print(f'{four} - {allTotals}')
            with open('STANDINGHISTORY.txt', 'a') as f:
                today = date.today()
                today2 = str(today)
                f.write(f' {four} - {allTotals}, ')
                f.write(today2)
                f.write('\n')
                f.write('\n')
                

def updateHistory(team, total):

        with open('STANDINGHISTORY.txt', 'a') as f:
            f.write(f' {team} - {total}, ')
        print("TEST") # to disable above appending




pointsPerTeam()




