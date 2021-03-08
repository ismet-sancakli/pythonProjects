from game_data import data
import random
from art import logo,vs
from replit import clear

def random_account():
# Get data from random account
  return random.choice(data)

def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_format, b_format):
  if a_format > b_format:
    return guess == "a"
  else:
    return guess == "b"
  

def game():
  print(logo)

  score = 0
  a_account= random_account()
  b_account = random_account()
  is_continue = True

  while is_continue:
    a_account = b_account
    b_account = random_account()

    while a_account == b_account:
      b_account = random_account()
    
    print(f"Compare A : {format_data(a_account)}")
    print("           -------------")
    print(vs)
    print(f"Compare B : {format_data(b_account)}")
    print("           -------------")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_account = a_account["follower_count"]
    b_follower_account = b_account["follower_count"]
    is_correct = check_answer(guess, a_follower_account, b_follower_account)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score = {score}.")
    else:
      is_continue = False
      print(f"Oh sorry. That is wwrong. Final score is = {score}")

game()

