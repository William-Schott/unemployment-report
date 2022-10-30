from getpass import getpass

API_KEY = getpass("Please input your AlphaVantage API Key: ") 
#PCBWXAJKUC99DFN6

import requests
import json
from pprint import pprint

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)
print(type(parsed_response))
pprint(parsed_response)


#Part A
print("-------------------------")
print("LATEST UNEMPLOYMENT RATE:")
#print(data[0])
print(f"{data[0]['value']}%", "as of", data[0]["date"])