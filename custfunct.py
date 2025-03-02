"""
Garrett Safsten, Ryan Baldwin, Jack Mair, Tanner Crookston
Section 003
This is a game simulation where we use 5 custom functions. A home and opposing team are chosen to play eachother. 
A certain number of games are chosen and scores are randomly generated. 
The results are posted at the end with an indication of a win or loss.
"""

import random 

# This is our introductory message to the user.
print("\nHello and welcome to our game simulation! You get to choose a home and opposing team to play eachother. You will choose how many games they will play and scores will be randomly chosen for each team in each game. The results will be posted at the end. But first let's get your name!")
name = input("\nWhat is your first name(eg. 'John')? ")
# This is a custom function that when it is called will always display "Hey(and then the users name.)"
def first_name(fName) :
    return fName

print("\nHey" + " " + first_name(name) + " " + "Welcome to the game!")


# This function asks the user to select a team and returns it
def select_team():
    team = input("\n" + first_name(name) + " enter the team name here: ")
    return team

# This function generates random scores and determines if the home team won or lost
def game() :
    score1 = 0
    score2 = 0
    status = None

    while score1 == score2 :
        score1 = random.randrange(0, 10)
        score2 = random.randrange(0, 10)

    if score1 > score2 :
        status = "W"
    if score2 < score2 :
        status = "L"

    list_record = [score1, score2, status]

    return list_record

# This is a dictionary storing all the team names.
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
print("\nPlease choose a home team from the following selections and type it exactly as displayed: \n")
print_teams()

sHomeTeam = select_team()

# This takes the home team out of the dictionary
# The while loop is so that the user cannot continue until they choose a team from the list
bContinue = False
while bContinue != True :
    if sHomeTeam not in dictTeams :
        print("\nWhoops, I think you mistyped. Try again and type the team name exactly as it is spelled.")
        sHomeTeam = select_team()
    else :
        bContinue = True
        dictTeams.pop(sHomeTeam)

# Displays choices and asks user to select an opponent
print("\nNow choose an opponent from the following selections and type it exactly as displayed: \n")
print_teams()

sAwayTeam = select_team()

# Makes sure the opponent team can be used and outputs the selections
# The while loop is so that the user cannont continue until they choose a team from the list
bContinue = False
while bContinue != True :
    if sAwayTeam not in dictTeams :
        print("\nWhoops, I think you mistyped. Try again and type the team name exactly as it is spelled.")
        sAwayTeam = select_team()
    else :
        bContinue = True

print("\nAwesome" + " " + first_name(name) + " " + f"you have selected {sHomeTeam} as your home team and {sAwayTeam} as your opponent!")

# Loop to play multiple games
game_count = int(input("\nHow many games would you like to simulate" + " " + first_name(name) + "? "))
lstResults = []

for _ in range(game_count):
    lstResults.append(game())

# Function to display final results
def print_results(results, home_team, away_team):
    print("\n" + first_name(name) + " here are your game results:")
    for i, result in enumerate(results):
        print(f"Game {i + 1}: {home_team} {result[0]} - {away_team} {result[1]} ({'Win' if result[2] == 'W' else 'Loss'})")

# Print all game results
print_results(lstResults, sHomeTeam, sAwayTeam)
print("\n")
