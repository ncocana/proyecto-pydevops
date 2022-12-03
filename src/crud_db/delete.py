import requests
import json

def deleteDocs():
    
    url = "https://data.mongodb-api.com/app/data-nxnpm/endpoint/data/v1/action/deleteOne" 

    payload = json.dumps({
    "collection": "bikes",
    "database": "rental_bikes",
    "dataSource": "SANDBOXX",
    "filter": {
        "type": "name bike"
    }
    })
    
    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'jNdMKZt2JmBwtYFJSwB8iRRx7M7OVqk0d1fPLuzaMDpLCkWOG7V5jgClzEYUKfV7', 
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    result = json.loads(response.text)
    
    return result


if __name__ == "__main__": 
  try:
    print(deleteDocs())
  except KeyError:
    print("This file haven't been deleted")
