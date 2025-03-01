# Ryan Baldwin
# This part accounts for step 3
"""
Display list of all teams and allow the user to 
choose a team using a menu. Call the function again to 
let the user choose the opponent but do not display the team 
they chose previously. Remove that team from the list. 
Allow the user to select an opponent, and return team name. 
This function should receive a parameter but give it a 
default value if none is passed. You can use this function 
for both choosing the home team and the opponent team.
"""

import random 

# This function asks the user to select a team and returns it
def select_team():
    team = input("\nPlease enter the team name here: ")
    return team

# This function generates random scores and # This function generates random scores and determines if the home team won or lost
def game() :
    score1 = 0
    score2 = 0
    status = None

    while score1 == score2 :
        score1 = random.randrange(0, 99)
        score2 = random.randrange(0, 99)

    if score1 > score2 :
        status = "W"
    if score2 < score2 :
        status = "L"

    list_record = [score1, score2, status]

    return list_record

dictTeams = {
    "Arizona": "Arizona",
    "Arizona State": "Arizona State",
    "Baylor": "Baylor",
    "BYU": "BYU",
    "UCF": "UCF",
    "Cincinnati": "Cincinnati",
    "Colorado": "Colorado",
    "Houston": "Houston",
    "Iowa State": "Iowa State",
    "Kansas": "Kansas",
    "Kansas State": "Kansas State",
    "Oklahoma State": "Oklahoma State",
    "TCU": "TCU",
    "Texas Tech": "Texas Tech",
    "Texas": "Texas",
    "Utah": "Utah",
    "West Virginia": "West Virginia"
}

# This part displays teams and calls the function for the user to select a team
print("Please choose a team from the following selections: \n")
for iCount in dictTeams:
    print(dictTeams[iCount])

sHomeTeam = select_team()

# This takes the home team out of the dictionary
bContinue = False
while bContinue != True :
    if sHomeTeam not in dictTeams :
        print("Error: please select a team from the above list")
        sHomeTeam = input("\nPlease enter the team name here: ")
    else :
        bContinue = True
        dictTeams.pop(sHomeTeam)

# Displays choices and asks user to select an opponent
print("\nNow choose an opponent from the following selections: ")
for iCount in dictTeams:
    print(dictTeams[iCount])

sAwayTeam = select_team()

# Makes sure the opponent team can be used and outputs the selections
bContinue = False
while bContinue != True :
    if sAwayTeam not in dictTeams :
        print("Error: please select a team from the above list")
    else :
        bContinue = True

print(f"\nYou have selected {sHomeTeam} and {sAwayTeam} as your team and opponent!")

lstResults = game()

