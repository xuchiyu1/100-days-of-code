# =========================================================
# Day 9 - Blind Auction Project
# Angela Yu 100 Days of Code
#
# Concepts Used:
# - Functions
# - Dictionaries
# - While loop
# - If / Else
# - Local variables
# - Parameter passing
# - State control using boolean flag
# =========================================================

import os


# -----------------------------
# Function: clear screen
# -----------------------------
def clear():
    """
    Clear the console screen.
    Compatible with Windows and Mac/Linux.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


# -----------------------------
# Function: find highest bidder
# -----------------------------
def find_highest_bidder(bidding_record):
    """
    Find the highest bidder from a dictionary.
    
    Parameter:
        bidding_record (dict):
            key = bidder name
            value = bid amount
    
    Logic:
        1. Initialize highest_bid = 0
        2. Loop through dictionary
        3. Compare each bid
        4. Update winner
    """

    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print("\nAuction Finished.")
    print(f"The winner is {winner} with a bid of ${highest_bid}")


# =========================================================
# Main Program Starts Here
# =========================================================

print("Welcome to the Secret Auction Program!")

# Dictionary to store all bids
bids = {}

# Boolean flag to control loop
bidding_finished = False


while not bidding_finished:

    name = input("What is your name? ")
    price = int(input("What is your bid? $"))

    # Store bid into dictionary
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)

    elif should_continue == "yes":
        clear()

    else:
        print("Invalid input. Ending auction.")
        bidding_finished = True
        find_highest_bidder(bids)
