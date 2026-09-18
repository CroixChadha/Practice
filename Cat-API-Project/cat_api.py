import requests
import json
import os
import sys
from flask import flask


# changed the api to the cat facts api
#request to the API for a fact
def get_cat_fact():
    cat_fact_request = requests.get('https://catfact.ninja/fact').json()
    print(json.dumps(cat_fact_request, indent=2))

def get_cat_breeds():
    cat_breed_request = requests.get('https://catfact.ninja/breeds').json()
    print(json.dumps(cat_breed_request, indent=2))

choice = input("What would you like to choose?")