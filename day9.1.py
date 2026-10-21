# use print("/n" * 100) to "Clear" the board
import random
print( r'''
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
''')
print("welcome to the bidding station! A shitty way to bid on a random item for no reason!")
# TODO-1: Ask the user for input
items = ["Lamp", "Toilet Paper", "Candle", "Hand Sanitizer", "Phone case that doesnt fit your phone", "Empty can of sprite", "Thumbtack", "Glue", "Dog toy", ]
item_choice = random.choice(items)
print("Todays item to bid on is: |", item_choice, "|  Go nuts...")
bids = {}
def ask():
    name = input("Please enter your name: ")

    bid = int(input("Please enter your bid: "))
    if bid > 100:
        print(f"really? That much for {item_choice}?")
        print("\n" * 7)
    bids[name] = bid
    again = input("Are there any other bidders? y/n: ")
    if again == "y":
        print("\n"* 50)
        print(f"The item we are bidding on is | {item_choice} | dont lose all of your money...")
        ask()
    elif again == "n":
        print("\n" * 7)
        winner = max(bids, key=bids.get)
        print(f"The winner is {winner}, with a bid of ${bids[winner]}")
        print(f"I cant believe you spent that much on {item_choice}, but hey its your life.")

    else:
        print("You Won the bid! ")
ask()
# TODO-2: Save data into dictionary {name: price}


# TODO-3: Whether if new bids need to be added

# TODO-4: Compare bids in dictionary