import sys

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
accepted_inputs = ["decode", "encode"]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
if direction not in accepted_inputs:
    print("not a valid option, try again!")
    sys.exit()
    
text = list(input("Type your message:\n").lower())
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs. - DONE
def encrypt(original_text, shift_amount):
    shifted = []

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet 
#  by the shift amount and print the encrypted text. - DONE
    for i in original_text:
        if i in alphabet:
            index = alphabet.index(i)
            shifted.append(alphabet[((index + shift_amount) % 26)])
        else:
            shifted.append(i)
        
    print(*shifted, sep='')    
        
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a message.
if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    encrypt(text, -shift)

    
    