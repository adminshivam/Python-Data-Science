
import sys
import random
from enum import Enum

class RPS(Enum):
  ROCK = 1
  PAPER = 2
  SCISSORS = 3

player = input("Enter 1 for rock, 2 for paper, 3 for scissors\n");
player = int(player)
print("")
print("Player selected : " + str(RPS(player)).replace('RPS.', ''))

if(player < 1 or player > 3):
  sys.exit("Player value must be between 1 and 3")

computer = random.choice("123")
computer = int(computer)

print("Computer selected : " + str(RPS(computer)).replace('RPS.', ''))

if(player == computer):
  print("Tie")
elif player == 1 and computer == 3:
  print("Player wins")
elif player == 2 and computer == 1:
  print("Player wins")
elif player == 3 and computer == 2:
  print("Player wins")
else:
  print("Computer wins")
sys.exit()
