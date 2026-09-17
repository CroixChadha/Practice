import requests
import json
import os
import sys


# changed the api to the cat facts api
# take input to ask what the person wants to see.
type_of_request = input("What would you like to see? Type 1 for cat facts. Type 2 for breeds. Type 3 to exit ")
# check for the the response type and append the param to the base url - OPTMIZE THIS
if type_of_request == str(1):
    param = "facts"
elif type_of_request == str(2):
    param = "breeds"
else:
    print("You selected Exit, bye!")
    sys.exit()
    
request = requests.get('https://catfact.ninja/' + param).json()
print(json.dumps(request, indent=2))