import requests, os

# Retrieve your API credentials from the .env file
if os.getenv("API_KEY") is None or os.getenv("API_KEY") == "":
    print("ERROR! Make sure you have created your .env file with your API credentials (look for the .evn.example as an example and replace it with your own API credentials that you got from RapidAPI)")
    exit(1)

# Get credentials from the .env file
API_HOST = os.getenv("API_HOST")
API_KEY = os.getenv("API_KEY")

# continue with your application here
userInput=input("What term do you want to look for?") 

import requests

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define?term=" +userInput

headers = {
    'x-rapidapi-host': API_HOST,
    'x-rapidapi-key': API_KEY
}

response = requests.request("GET", url, headers=headers)
response=response.json()
#for x in response["list"]:

print(response["list"][0]["definition"]) 