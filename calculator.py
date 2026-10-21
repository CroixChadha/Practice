from art import logo

def add(n1, n2):
    return n1 + n2
#TODO: write out the other functions - subtract, multiply and divide.
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
# take the user input to decide the operation
def calc():
    print(logo)
    begin = True
    first_number = int(input("What is the first number? "))

#TODO - Add these four functions into a dictionary as the values. Keys = "+", "-", "*", "/".
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

#TODO use the dictionary operations to perform the calculations. multiply 4 * 8 using the dictionaries
    while begin:
        print("+")
        print("-")
        print("*")
        print("/")

        operation = input("What operation would you like to do? ")
        while operation not in operations:
            print("Please enter a valid operation")
            operation = input("What operation would you like to do? ")
        second_number = int(input("What is the second number?: "))

        result = operations[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")

        again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if again == "n":
            print("ok \n")
            calc()
        elif again == "y":
            first_number = result
calc()