#Make Lists of Players in NBA Teams with Stats
from bs4 import BeautifulSoup
import requests
page = requests.get("https://www.espn.com/nba/team/stats/_/name/mia/miami-heat")
soup = BeautifulSoup(page.text, 'html.parser')
#creates file, writes Prettified HTML to file
file = open('myfile.html', 'w')
#looks through html, grabs players to make dictionary of players to positions
rosterCount = 0
for element in soup.find_all(class_="Table__TR Table__TR--sm Table__even"):
    if(element.text == 'Total'):
        break
    rosterCount+=1
#Creates a number of players in Roster
rosterList = []
for element in soup.find_all(class_="Table__TR Table__TR--sm Table__even"):
    temp = []
    if(element.text!='Total'):
        for el in element.text.split(' '):
            if el == "*":
                break
            else:
                temp.append(el)
        rosterList.append(temp)
        
    else:
        break
#Creates List of Players in Roster
statList = []
for element in soup.find_all(class_="Table__TD"):
    statList.append(element.text)
count = 0
statList = statList[rosterCount+1:13*rosterCount+rosterCount+1]
#Creates a List of stats to give to each player
n=0
for element in rosterList:
    element.append(statList[0+13*n:13+13*n])
    n+=1
print(rosterList)
#Adds stats to players on rosterList

class Player:
    def __init__(player,name, points,assists,rebounds):
        player.name = name
        player.points = points
        player.assists = assists
        player.rebounds = rebounds

#barebone for player object

