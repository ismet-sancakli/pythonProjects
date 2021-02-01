from replit import clear
#HINT: You can call clear() to clear the output in the console.
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bids ={}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_record = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_record:
      highest_record = bid_amount
      winner = bidder
  print(f"The winner is {winner} wth a bid of ${highest_record}")



while not bidding_finished:
  name = str(input("What is your name: "))
  price = int(input("What is your bid?:  $ "))
  bids[name] = price 
  should_countinue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if should_countinue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_countinue == "yes":
    clear()

