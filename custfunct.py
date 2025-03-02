"""
Garrett Safsten, Ryan Baldwin, Jack Mair, Tanner Crookston
Section 003

Description...
"""

import random 

# This is our introductory message to the user.
print("This is where the intro will go when we have actually finished the code")
name = input("What is your first name(eg. 'John')? ")
# This is a custom function that when it is called will always display "Hey(and then the users name.)"
def first_name(fName) :
    return fName

print("Hey" + " " + first_name(name) + " " + "Welcome to the game!")


""" 
What else is needed: either here or above the name input function, there needs to be an 
introductory message explaining the rules. At the bottom, there needs to be output that
shows the results of the game between the two teams. We also need one more function.

Whatever code makes the results at the end could probably be turned into a function.
"""

# This function asks the user to select a team and returns it
def select_team():
    team = input("\nPlease enter the team name here: ")
    return team

# This function generates random scores and determines if the home team won or lost
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

def print_teams():
    for iCount in dictTeams:
        print(dictTeams[iCount])

# This part displays teams and calls the function for the user to select a team
print("Please choose a team from the following selections: \n")
print_teams()

sHomeTeam = select_team()

# This takes the home team out of the dictionary
# The while loop is so that the user cannot continue until they choose a team from the list
bContinue = False
while bContinue != True :
    if sHomeTeam not in dictTeams :
        print("Error: please select a team from the above list")
        sHomeTeam = select_team()
    else :
        bContinue = True
        dictTeams.pop(sHomeTeam)

# Displays choices and asks user to select an opponent
print("\nNow choose an opponent from the following selections: ")
print_teams()

sAwayTeam = select_team()

# Makes sure the opponent team can be used and outputs the selections
# The while loop is so that the user cannont continue until they choose a team from the list
bContinue = False
while bContinue != True :
    if sAwayTeam not in dictTeams :
        print("Error: please select a team from the above list")
        sAwayTeam = select_team()
    else :
        bContinue = True

print(f"\nYou have selected {sHomeTeam} and {sAwayTeam} as your team and opponent!")

# Loop to play multiple games
game_count = int(input("How many games would you like to simulate? "))
lstResults = []

for _ in range(game_count):
    lstResults.append(game())

# Function to display final results
def print_results(results, home_team, away_team):
    print("\nGame Results:")
    for i, result in enumerate(results):
        print(f"Game {i + 1}: {home_team} {result[0]} - {away_team} {result[1]} ({'Win' if result[2] == 'W' else 'Loss'})")

# Print all game results
print_results(lstResults, sHomeTeam, sAwayTeam)


