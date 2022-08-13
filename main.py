#program id: rock paper scissors
#author: Geoffrey Zhang
#purpose: Use random number generator to play rock paper scissors with ai.

#allow code to roll a random number
from random import *

#starts the game off
play_again = input("Do you want to play rock, paper, scissor (y/n): ")

#the play again loop for the whole game
while (play_again == "y"):

  #player picks then ai rolls a number
  player_choice = input ("Pick rock paper or scissors: ")
  ai_choice = (randint(1,3))

  #setting each number with a value
  if(ai_choice == 1):
    ai_choice2 = "rock"
  elif(ai_choice == 2):
    ai_choice2 = "paper"
  else:
    ai_choice2 = "scissors"

  # if ai chose 1 (rock)
  if(ai_choice == 1):
    print (ai_choice2)
    if (player_choice == "paper" and ai_choice == 1):
      print ("You Win")
      play_again = input ("Play again?: ")
    if (player_choice == "scissors" and ai_choice == 1):
      print ("You lose")
      play_again = input ("Play again?: ")
    
  # if ai chose 2 (paper)
  if(ai_choice == 2):
    print (ai_choice2)
    if (player_choice == "rock" and ai_choice == 2):
      print ("You Lose")
      play_again = input ("Play again?: ")
    if (player_choice == "scissors" and ai_choice == 2):
      print ("You Win")
      play_again = input ("Play again?: ")

  # if ai chose 3 (scissors)
  if (ai_choice == 3):
    print (ai_choice2)
    if (player_choice == "rock" and ai_choice == 3):
      print ("You Win")
      play_again = input ("Play again?: ")
    if (player_choice == "paper" and ai_choice == 3):
      print("You Lose")
      play_again = input ("Play again?: ")
 
  if(player_choice == ai_choice2):
    print ("You Tied")
    play_again = input ("Play again?: ")
#ending remarks
print ("Thanks for playing bud.")