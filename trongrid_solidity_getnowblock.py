

import requests

url = "https://api.trongrid.io/walletsolidity/getnowblock"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers)

print(response.text)

