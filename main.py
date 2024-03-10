# Premise of the game : Roll a die, get a number from 1-6 
#if you get anything other than 1 : Take it and add to the total 
# You can decide how many times you can roll the dice 
# If you hit a 1 whatever total resets to 0
import random
PLAYERCOUNT =2

def printLineSeperator():
    print("----------------------------------------------------------------------------------")

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
           print(" You just rolled a 1! Your game is over.")
           printLineSeperator()
           break
        else :
           score += roll_result
        print(f"You have just rolled a {roll_result}. \n You have completed {roll_counter} ROLLS. \n Your Total score is  {score}.")
        printLineSeperator()

    print(f"You finished the game with a score of {score}. You rolled the dice {roll_counter} times.")
    printLineSeperator()
    return score, roll_counter



def main():
    print ("Welcome! This a 2 player game of PIG")
    playerNameList = []
    playerResultList= []
    #for i in range (1, PLAYERCOUNT):
    player_one_name = input("Please enter the name of Player 1:")
    printLineSeperator()
    player_two_name = input("Please enter the name of Player 2:")
    printLineSeperator()
    playerNameList.append(player_one_name)
    #playerNam
    playerOneResult=runPlayerGame(player_one_name)
    playerTwoResult=runPlayerGame(player_two_name)
    playerOneScore = playerOneResult[0]
    playerTwoScore = playerTwoResult[0]

    if playerOneScore > playerTwoScore :
        print(f"{player_one_name} WINS! with a score of {playerOneScore}. They rolled {playerOneResult[1]} times!")
        printLineSeperator()

    elif playerOneScore < playerTwoScore:
         print(f"{player_two_name} WINS! with a score of {playerTwoScore}. They rolled {playerTwoResult[1]} times!")
         printLineSeperator()
    else:
        print(f"It is a Tie!!!! Both pHalayers scored {playerTwoScore}.\n {player_one_name} rolled {playerOneResult[1]} times. \n {player_two_name} rolled {playerTwoResult[1]} times.")
        printLineSeperator()

    print("Thank you for playing! GOOD BYE!!!")

  
main()

     




