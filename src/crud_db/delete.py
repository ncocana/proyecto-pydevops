import requests
import json

def deleteDocs():
    
    url = "https://data.mongodb-api.com/app/data-nxnpm/endpoint/data/v1/action/deleteOne" 

    payload = json.dumps({
    "collection": "bikes",
    "database": "rental_bikes",
    "dataSource": "SANDBOXX",
    "filter": {
        "type": "insert bike name"
    }
    })
    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'jNdMKZt2JmBwtYFJSwB8iRRx7M7OVqk0d1fPLuzaMDpLCkWOG7V5jgClzEYUKfV7', 
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    result = json.loads(response.text)
    
    assert isinstance(result, dict)
    
    value = list(result.values())
    for item in value:
        if item == 0:
            print('This file is not delete')
            return False
   
        if item == 1:
            print('this file has been deleted')
            return True


if __name__ == "__main__":
    
    deleteDocs()