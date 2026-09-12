import random

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

num_numbers = int(input("How many numbers do you want?"))
num_chars = int(input("How many Characters do you want?"))
num_sym = int(input("How many Symbols do you want?"))

amount_nums = []
amount_syms = []
amount_chars = []

for num in range(0, num_numbers):
    amount_nums.append(random.choice(numbers))

for sym in range(0, num_sym):
    amount_syms.append(random.choice(symbols))

for char in range(0, num_chars):
    amount_chars.append(random.choice(characters))

non_random = [amount_chars + amount_nums + amount_syms]

print(*non_random, sep='')