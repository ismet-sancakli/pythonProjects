rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

RPS = [rock , paper , scissors]
game_number = int(input("How many times will you play?"))

i = 0

while(i < game_number):
  your_choice = int(input("What do you choose? Type 0 is Rock, Type 1 is Paper, Type 2 is Scissors. "))
  
  i = i+1

  if (your_choice >= 3 or your_choice < 0):

    print("Invalid Number !! Try Again")
  else:


    print("Your choice is: " + RPS[your_choice])

    computer_choice =random.randint(0,2)
    print("Computer choice is: " + RPS[computer_choice])

    if your_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and your_choice == 2:
        print("You lose")
    elif computer_choice > your_choice:
        print("You lose")
    elif your_choice > computer_choice:
        print("You win!")
    elif computer_choice == your_choice:
        print("It's a draw")
    

