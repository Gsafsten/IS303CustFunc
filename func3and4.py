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

# This function generates random scores and 