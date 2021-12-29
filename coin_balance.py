
import requests
import sys

def transaction_test_coin(hex_address_owner):
    url_1 = "https://api.shasta.trongrid.io/v1/accounts/"
    url_2 = hex_address_owner
    url_3 = "/transactions" 
    url = url_1 + url_2 + url_3
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers)    
    
    print("transaction test coin")
    print(response.text)   


def getaccount_owner(hex_address_owner):
    url = "https://api.shasta.trongrid.io/wallet/getaccount"
    ss = hex_address_owner
    payload = {"address":ss}
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
	
    print("getaccount_owner")
    print(response.text)


if __name__ == '__main__':

    hex_address_owner = sys.argv[1]
    transaction_test_coin(hex_address_owner)
    getaccount_owner(hex_address_owner)
    
	
	
	
	   