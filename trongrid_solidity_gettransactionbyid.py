

import requests
import sys

def gettransactionbyid (txid):

    url = "https://api.trongrid.io/walletsolidity/gettransactionbyid"
    payload = {"value": txid}
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.text)

if __name__== "__main__":

    txid = sys.argv[1]
    gettransactionbyid (txid)