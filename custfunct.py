# '''
# Garrett Safsten
# Section 003
# This program will use user input for a home team name, number of season games, and each opposing team that the home team will play.
# All of the information from the user and the generated numbers will be stored in lists and a dictionary. 
# Then the program will generate random scores with the user input and display each game with the teams and the score.
# The season record will also be displayed based and a message depending on the percentage of wins for the year.
# '''
# # Here are each of the custom functions that we will use to avoid repeating the same code multiple times.


# #This defines the random variable and allows me to assign a random variable
# import random 

# #These are list for which we will store data into.
# tnames = []
# hscores = []
# ascores = []
# win = []

# # This is a dictionary where we will store the list "tnames" inside.
# dictsoccerteams = {"tnames": []}



# #These are two questions to obtain user input for a team home name and the number of games played during the season.
# hTeam = input("\nWhat is the name of your home team? (ex.'BYU')\n")
# nhgames = int(input("\nHow many games will your home team play in a season? (ex. 5)\n"))

# # This sets the counter for the number of games so the counter knows where to start
# gamenum = 1

# # This is a loop to gather and store all the data we need for each season game.
# for icount in range(1, nhgames +1, 1) :
#     aTeam = input(f"\nWhat is the name of the away team for game {gamenum}? (ex.'USU')\n") # This asks for the name of the opposing team from the user.
#     gamenum = gamenum + 1 # This increments the number of games depending on how many games are entered byt the user for the season. Ex. game 1, game 2, etc.
#     hscore = random.randrange(1,10) # This generates a random home score for each game.
#     ascore = random.randrange(1,10) # This generates a random away score for each game
#     while hscore == ascore : # This while loop ensures there is not a tie.
#         hscore = random.randrange(1,10)
#         ascore = random.randrange(1,10)   
#     dictsoccerteams["tnames"].append(aTeam) # Our dictionary storing the list tnames/.
#     hscores.append(hscore) # A list storing the home team scores for each game.
#     ascores.append(ascore) # A list storing the away team scores for each game.
#     if hscore > ascore : # This if statement assigns a win for each game the home team wins.
#         hscore = "W"   
#     else :
#         pass
#     win.append(hscore) # A list storing the home team wins as a "W".
#     winscore = win.count("W")
#     losescore = nhgames - winscore # This calculate the number of games lost by the home team.
# print("\n") # This simply enhances the user experience by spacing out the output.
# # The following for loop and if statment print out each game with both teams scores.
# tnames = 0
# for game in range(nhgames) :
#     print(f"{hTeam}'s score: {hscores[game]} {dictsoccerteams["tnames"][game]}'s score: {ascores[game]}")
#     tnames = tnames + 1
# print(f"\n\nFinal season record: {winscore} - {losescore}") # Prints the season record and a message based on the percentage of wins.
# if (winscore/nhgames) >= .75 :
#    print("Qualified for the NCAA Women's Soccer Tournament!\n")
# elif (winscore/nhgames) >= .50 :
#     print("You had a good season!\n")
# else :
#     print("Your team needs to practice!\n")

"""
Garrett Safsten, Ryand Baldwin, Jack Mair, Tanner Crookston
Section 003

Description...
"""

# This is our introductory message to the user.
print("This is where the intro will go when we have actually finished the code")
name = input("What is your first name(eg. 'John')? ")
# This is a custom function that when it is called will always display "Hey(and then the users name.)"
def first_name(fName) :
    return fName

print("Hey" + " " + first_name(name) + " " + "Welcome to the game!")




