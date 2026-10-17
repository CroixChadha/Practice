# Croix's Wordle - Why use the new york times wordle, if you can just use a shitty terminal only version? 
import random

print(r"""
 __        __   ___   ____   ____   _      _____ _
 \ \      / /  / _ \ |  _ \ |  _ \ | |    | ____| |
  \ \ /\ / /  | | | || |_) || | | || |    |  _| | |
   \ V  V /   | |_| ||  _ < | |_| || |___ | |___|_|
    \_/\_/     \___/ |_| \_\|____/ |_____||_____(_)

       W E L C O M E   T O   W O R D L E !

          [ W ][ O ][ R ][ D ][ L ][ E ]

             Guess the 5-letter word!
                 You have 6 tries!
""")
start = input("Would you like to start? y/n ")
#list of words
words = ["huzza", "muzzy", "juicy", "enzym", "jerky", "gizmo", "gyoza", "booty", "booze"]
#randomize the word choice
word_to_guess = list(random.choice(words))
#temp print statement
placeholder = []

#TODO - Get user input for the letters
user_guess = []
guess = user_guess.append(input("What letter do you choose? "))
#TODO - Print the chosen word with placeholders instead of the actual word "XXXXX"
for letter in word_to_guess:
    placeholder.append("X")
if start == "y":
    print(*placeholder, sep='')


#TODO - create a function to run through the wordle process
def wordle():
    for guess in user_guess:
        if guess in word_to_guess:
            placeholder.index()
# User gets 5 attempts to guess
# Every incorrect guess the user is shown how many lives they have
# The placeholders should be changed to the proper word after correct guess


