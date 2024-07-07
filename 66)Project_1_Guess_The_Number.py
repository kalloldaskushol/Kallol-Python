# Project_1_Guess_The_Number
# Computer will select a number and user has to guess it
# IF the user guess a number which is larger than the target number then print
# Number is larger than the target
# If the user gueeses a nummber which is smaller than the target number than print
# Number is smailler than the target

import random 

target = random.randint(1,100)

while True:
    user_choice = int(input("Guess the number or quit the game="))

    if(user_choice == "quit"):
        break

    if(user_choice==target):
        print("Yoo!You Won the game,Congoooo!")
        break
    
    elif(user_choice<target):
        print("To small! pick a bigger guess")
    else:
        print("To big! pick a smaller guess")

print("_____GAME_OVER______")