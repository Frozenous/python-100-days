import art
print(art.logo)
user_bids = {
}
users_to_bid = True
while users_to_bid:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    user_bids[name] = bid
    others = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if others == "no":
        users_to_bid = False
    elif others == "yes":
        print("\n"*20)
highest_bid = max(user_bids.values())
winner = max(user_bids, key=user_bids.get)
print(f"The winner is {winner} with a bid of ${highest_bid}")
