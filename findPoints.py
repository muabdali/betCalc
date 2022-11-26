import csv
import pandas as pd

# teams
musTeam = ["Netherlands","Senegal","England","Wales","Argentina","Mexico","France","Australia","Germany","Spain","Canada","Belgium","Brazil","Cameroon","Portugal","Uruguay"]
aliTeam = ["Netherlands","Ecuador","Wales","England","Argentina","Saudi Arabia","Denmark","France","Germany","Spain","Belgium","Canada","Brazil","Serbia","Ghana","Portugal"]
shuaybTeam = ["Netherlands","Ecuador","England","Wales","Argentina","Poland","Australia","Denmark","Germany","Spain","Croatia","Belgium","Brazil","Serbia","Portugal","Uruguay"]
maxemTeam = ["Netherlands","Senegal","England","Wales","Argentina","Mexico","Denmark","Tunisia","Germany","Spain","Belgium","Canada","Brazil","Switzerland","Portugal","Uruguay"]

allTeams = [musTeam,aliTeam,shuaybTeam,maxemTeam]

def findPointdF(chosenTeam):
    global pointTotal
    pointTotal = 0
    countTotal = 0
    df = pd.read_csv("combinedStandings01.csv")
    for country in chosenTeam:
        if country in df.values:
            pointTotal = pointTotal + 1
    print(pointTotal)
    return pointTotal



def findPerfects(chosenTeam):
    global pointFirstPerfectTotal
    pointFirstPerfectTotal = 0
    dfFirst_2 = pd.read_csv("combinedStandings01.csv")
    FirstTeams = dfFirst_2.iloc[::2]
    FirstListTeams = chosenTeam[::2]
    for country in FirstListTeams:
        if country in FirstTeams.values:
            pointFirstPerfectTotal = pointFirstPerfectTotal + 2
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
            pointSecondPerfectTotal = pointSecondPerfectTotal + 2
    print(pointSecondPerfectTotal)
    return pointSecondPerfectTotal


def findAllPoints(FUNCTIONCHOSEN):
    findPointdF(chosenTeam=FUNCTIONCHOSEN)
    findPerfects(chosenTeam=FUNCTIONCHOSEN)
    findSecondPerfects(chosenTeam=FUNCTIONCHOSEN)
    return




def pointsPerTeam():
    one = 'musTeam'
    two = 'aliTeam'
    three = 'shuaybTeam'
    four = 'maxemTeam'
    pointCounter = 0
    for team in allTeams:
        findAllPoints(team)
        allTotals = pointTotal + pointFirstPerfectTotal + pointSecondPerfectTotal
        pointCounter = pointCounter + 1
        if pointCounter == 1:
            print(f'{one} - {allTotals}')
        elif pointCounter == 2:
            print(f'{two} - {allTotals}')
        elif pointCounter == 3:
            print(f'{three} - {allTotals}')            
        elif pointCounter == 4:
            print(f'{four} - {allTotals}')

findAllPoints(maxemTeam)

#pointsPerTeam()