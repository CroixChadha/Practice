import requests
import json
import os
import sys


# changed the api to the cat facts api
# take input to ask what the person wants to see.
type_of_request = input("What would you like to see? Type 1 for a cat fact. Type 2 for breeds. Type 3 to exit ")
# check for the the response type and append the param to the base url - OPTMIZE THIS

#request to the API for a fact
def get_cat_fact():
    cat_fact_request = requests.get('https://catfact.ninja/fact').json()
    print(json.dumps(cat_fact_request, indent=2))
    