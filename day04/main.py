import random
import sys

#Rock = 0
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
#Paper = 1
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
#Scissors = 2
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

player_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: \n'))
if 0 <= player_choice <= 2:
    print(game_images[player_choice])
else:
    print('Invalid Choice')
    sys.exit()

computer_choice = random.randint(0,2)
print(game_images[computer_choice])
#Player chooses Rock
if player_choice == 0:
    if computer_choice == 0:
        print('Draw')
    elif computer_choice == 1:
        print('You Lose!')
    elif computer_choice == 2:
        print('You Win!')
#Player chooses Paper
elif player_choice == 1:
    if computer_choice == 0:
        print('You Win!')
    elif computer_choice == 1:
        print('Draw!')
    elif computer_choice == 2:
        print('You Lose!')
#Player Chooses Scissors
elif player_choice == 2:
    if computer_choice == 0:
        print('You Lose!')
    elif computer_choice == 1:
        print('You Win!')
    elif computer_choice == 2:
        print('Draw!')
