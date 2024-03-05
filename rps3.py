import sys
import random
from enum import Enum
def play_rps():
    
    class RPS(Enum):
      ROCK =1
      PAPER =2
      SCISSORS =3
    playerchoice=input("\nEnter...\n1 for rock,\n2 for paper,\n3 for scissors:\n\n")
    if playerchoice not in ["1","2","3"]:
        print("You must enter 1,2 or3.")
        return play_rps()
    player=int(playerchoice)
    if player <1 or player>3:
        sys.exit()
   
    computerchoice=random.choice("123")
    computer=int(computerchoice)
    print("\nYou choose" + str(RPS(player)).replace('RPS.','') + ".")
    print("David choose" + str(RPS(computer)).replace('RPS.','') + ".\n")
    if player == 1 and computer == 3:
     print("🎉You win!")
    elif player == 2 and computer == 1:
     print("🎉You win!")
    elif player == 3 and computer == 2:
     print("🎉You win!")
    elif player == computer:
     print("😲Tie game!")
    else:
     print("🐍 python wins!")
    print("\nPlay again?")
    while True: 
        playagain=input("\nY for yes or\nQ to quit\n")
        if playagain.lower() not in ["y","q"]:
           continue
        else:
            break
    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🎉🎉🎉🎉🎉")
        print("Thank you for playing !\n")
        sys.exit("Bye! ")
play_rps()