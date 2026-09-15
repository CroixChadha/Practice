import requests
import json
import os
from settings import API_KEY

#date input
date = input("Please type the date out like this: YYYY-MM-DD ")

#parameter dictionary
params = {
    "api_key": API_KEY,
    "date": date,
    "title": '',
}
# requests to go to the api 
request = requests.get('https://science.nasa.gov/wp-json/wp/v2/apod-basic?api_key=API_KEY')
print(json.dumps(request, indent=2))