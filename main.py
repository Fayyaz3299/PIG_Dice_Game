# Premise of the game : Roll a die, get a number from 1-6 
#if you get anything other than 1 : Take it and add to the total 
# You can decide how many times you can roll the dice 
# If you hit a 1 whatever total resets to 0

import random


PLAYERCOUNT = 4


ARRAYLOCATION_NAME = 0
ARRAYLOCATION_SCORE = 1
ARRAYLOCATION_ROLLS = 2


def printLineSeperator():
    print("----------------------------------------------------------------------------------")

def printPlayerDetails(player):
    printLineSeperator()
    print(f"Player Name : {player[ARRAYLOCATION_NAME]}.\n Player Score : {player[ARRAYLOCATION_SCORE]}. \n Number of rolls by the player : {player[ARRAYLOCATION_ROLLS]}.")
    printLineSeperator()

    
def roll ():
    number = random.randint(1,6)
    return number

def runPlayerGame(player_name):
    score = 0;
    roll_counter =0;
    while True:
        print (f"{player_name}!!! It is your turn! \n Your current score is {score}.")
        printLineSeperator()
        answer = input("Press enter to roll the die (q to quit):")
        printLineSeperator()
        if answer == "q":
            break
        roll_result =  roll()
        roll_counter += 1
        if roll_result == 1:
           score =0
           print("You just rolled a 1! Your game is over.")
           printLineSeperator()
           break
        else :
           score += roll_result
        print(f"You have just rolled a {roll_result}. \n You have completed {roll_counter} ROLLS. \n Your Total score is  {score}.")
        printLineSeperator()

    print(f"You finished the game with a score of {score}. You rolled the dice {roll_counter} times.")
    printLineSeperator()
    return player_name, score, roll_counter


def main():
    print (f"Welcome! This a {PLAYERCOUNT} player game of PIG")
    playerNameList = []
    playerResultList= []
    highestScore = 0
    for i in range (0, PLAYERCOUNT):
        name = input(f"Please enter the name of Player {i+1}: ")
        printLineSeperator()
        playerNameList.append(name)
    
    for i in range (0, PLAYERCOUNT):
        playerResult = (runPlayerGame(playerNameList[i]))
        if (playerResult[ARRAYLOCATION_SCORE] > highestScore):
            highestScore = playerResult[ARRAYLOCATION_SCORE]
        playerResultList.append(playerResult)
        
        
    winnersList =[]
    for i in range (0, PLAYERCOUNT):
        if highestScore == playerResultList[i][ARRAYLOCATION_SCORE]:
            winnersList.append(playerResultList[i])

    if len(winnersList) == 1 :
        printLineSeperator()
        print(f"{winnersList[0][ARRAYLOCATION_NAME]} WINS!")
        printPlayerDetails(winnersList[0]) 
        
    else:
        printLineSeperator()
        print(f"It is a TIE! The players scored:")

        for i in range (len(winnersList)):
            printPlayerDetails(winnersList[i])
        printLineSeperator()
       

    print("Thank you for playing! GOOD BYE!")
  
main()

     




