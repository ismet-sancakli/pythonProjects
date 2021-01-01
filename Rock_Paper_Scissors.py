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

your_choice = int(input("What do you choose? Type 0 is Rock, Type 1 is Paper, Type 2 is Scissors. "))
print("Your choice is: " + RPS[your_choice])

computer_choice =random.randint(0,2) 
print("Computer choice is: " + RPS[computer_choice])

if ((your_choice == 0 and computer_choice == 1) or (computer_choice == 0 and your_choice == 2) or (your_choice == 1 and computer_choice == 2)):
  print("You lost !")
elif((your_choice == 0 and computer_choice == 2) or (computer_choice == 2 and your_choice == 3) or (your_choice == 1 and computer_choice == 0)):
  print("\n*** You win !!! ***\n")
elif (your_choice == computer_choice):
  print("It is a draw")
else:
  print("Try Again !!! Invalid Number")  

