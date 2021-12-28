
import requests


url = "https://api.shasta.trongrid.io/wallet/generateaddress"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers)
    
print(response.text)  
   

 
   