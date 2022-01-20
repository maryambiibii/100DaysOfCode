#The Secret Auction Program
from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

all_bidders = {}
other_bidders = "yes"

while other_bidders == "yes":
    name = input("Enter your name for bidding: ")
    bid_value = int(input("Enter your value for bidding: $"))
    all_bidders[name] = bid_value
    other_bidders = input("Is there any other bidder. Type 'yes' if there is, and 'no' if do not? ").lower()
    clear()

highest_bidding_value = 0
for bidders in all_bidders:
    if all_bidders[bidders] > highest_bidding_value:
        highest_bidding_value = all_bidders[bidders]

for bidders in all_bidders:
    if all_bidders[bidders] == highest_bidding_value:
        print(f"Bid is won by {bidders} with ${all_bidders[bidders]}")
