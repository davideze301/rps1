import sys
import random
from enum import Enum
def rps():
    game_count=0
    player_wins=0
    python_wins=0
    def play_rps():
        nonlocal player_wins
        nonlocal python_wins
        
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
        def decide_winner(player,computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins+=1
                return"🎉You win!"
            elif player == 2 and computer == 1:
                  player_wins +=1
                  return"🎉You win!"
            elif player == 3 and computer == 2:
                  player_wins +=1
                  return"🎉You win!"
            elif player == computer:
                return"😲Tie  game!"
            else:
                python_wins +=1
                return"🐍 python wins!"
        game_result=decide_winner(player,computer)
        print(game_result)
        nonlocal game_count
        game_count += 1
        print("\n Game count: " + str(game_count))
        print("\n Player wins: " + str(player_wins))
        print("\n python wins: " + str(python_wins))
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
    return play_rps()
play=rps()
play()
