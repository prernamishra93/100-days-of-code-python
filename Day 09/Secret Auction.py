from art import logo

print(logo)
print("Welcome to the private bidding auction")

auction_info = {}
auction = True

def find_highest_bid(auction_info):
    winner = ""
    highest_bid = 0
    for bidder in auction_info:
        bid_amount = auction_info[bidder]
        if highest_bid < bid_amount:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with a bid of {highest_bid}")

while auction :
    name  = input("What is your name?: ")
    bid = float(input("How much would you like to bid?: $"))
    auction_info[name] = bid

    should_continue = input("Are there any other bidders for this auction? Type 'yes' or 'no'.\n").lower()
    if should_continue == 'no':
        auction = False
        find_highest_bid(auction_info)
    else:
        print("\n" * 20)
    
