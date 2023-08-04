import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Some code here...

# Clear the console output
clear_console()

# Continue with the rest of the code...


bids = {}
bidding_finished = False

def find_highest_bidder(bidding_recond):
    highest_bid = 0
    for bidder in bidding_recond:
        bid_amount = bidding_recond[bidder]
        if int(bid_amount) > int(highest_bid):
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input('What is your name?')
    price = input("What is your bid? $")
    bids[name]= price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == "no":
      bidding_finished = True
      find_highest_bidder(bids)
    elif should_continue == 'yes':
      clear_console()




