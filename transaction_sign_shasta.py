

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

def transaction_sign(amount, privatekey, hex_address_owner, hex_address_to, signature_str):
    url = "https://api.shasta.trongrid.io/wallet/gettransactionsign"
    raw_data_1 = "{\"contract\":[{\"parameter\":{\"value\":{\"amount\":"
    raw_data_2 = amount
    raw_data_3 = ",\"owner_address\":\""
    raw_data_4 = hex_address_owner
    raw_data_5 = "\",\"to_address\":\""
    raw_data_6 = hex_address_to
    raw_data_7 = "\"},\"type_url\":\"type.googleapis.com/protocol.TransferContract\"},\"type\":\"TransferContract\"}],\"ref_block_bytes\":\"5e4b\",\"ref_block_hash\":\"47c9dc89341b300d\",\"expiration\":1591089627000,\"timestamp\":1591089567635}"
    all_raw_data = raw_data_1 + raw_data_2 + raw_data_3 + raw_data_4 + raw_data_5 + raw_data_6 + raw_data_7
    signatures = []
    signatures.append(signature_str)
    payload = {
        "transaction": {
            "raw_data": all_raw_data,
            "raw_data_hex": "0a025e4b220847c9dc89341b300d40f8fed3a2a72e5a66080112620a2d747970652e676f6f676c65617069732e636f6d2f70726f746f636f6c2e5472616e73666572436f6e747261637412310a1541608f8da72479edc7dd921e4c30bb7e7cddbe722e121541e9d79cc47518930bc322d9bf7cddd260a0260a8d18e8077093afd0a2a72e",
            "signature": signatures
        },
        "privateKey": privatekey
    }
	
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }  

    response = requests.request("POST", url, json=payload, headers=headers)
    
    print("transaction_sign")  
    print(response.text)   
    
  
if __name__ == '__main__':
   
   amount = sys.argv[1]
   privatekey = sys.argv[2]
   hex_address_owner = sys.argv[3]
   hex_address_to = sys.argv[4]
   signature_str = sys.argv[5]
   
   
   transaction_test_coin(hex_address_owner)
   getaccount_owner(hex_address_owner)
   transaction_sign(amount, privatekey, hex_address_owner, hex_address_to, signature_str)
