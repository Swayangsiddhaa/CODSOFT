import random 

def play(your_choice,computer_choice): #This function determines the winner based on the choices made by the player and the computer.
    if(your_choice==computer_choice):  # The logic of the game is: Rock beats scissors, scissors beat paper, and paper beats rock.
        print("it is a tie")
    elif(your_choice == "rock" and computer_choice == "scissors") or \
        (your_choice == "paper" and computer_choice == "rock") or \
        (your_choice == "scissors" and computer_choice == "paper"):
        print("You win!")   
    else:
        print("You lose!")
        
#This function Starts the game by generating the computer's choice and comparing it with the player's choice.
def Start(your_choice): 
    Options = ["rock", "paper", "scissors"]
    computer_choice=random.choice(Options)
    print("Your option:",your_choice)
    print("Computer's choice:",computer_choice)
    play(your_choice,computer_choice)

#opening statement:-
print("Welcome friend! so let's start to play the game rock, paper, and scissors")
print("This game is You vs Computer")
print("The logic of the game is: Rock beats scissors, scissors beat paper, and paper beats rock.")
Options = ["rock", "paper", "scissors"]
print("This is the options from where you can choose what you want",Options)

#This loop plays the game until user or player says no.
#And it also checks if the given input is valid or not.
#Then it starts the game.
while (True):
        your_choice=input("Write what you want to choose from options:").lower()
        if(your_choice in Options):
            Start(your_choice) 
        elif(your_choice not in Options):
            a=input("Invalid input!, please see the options list and choose correctly:")
            if(a in Options):
                Start(a)
            else:
                print("Please see the valid options in our option list and then choose to play again.")
                continue
        b=input("Do you want to play next round? only:-(yes or no):-").lower()
        if(b=="no"):
            break
print("Thank you for participating.")
