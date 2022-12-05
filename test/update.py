import requests
import json

def updateOne():
    url = "https://data.mongodb-api.com/app/data-nxnpm/endpoint/data/v1/action/updateOne"
    payload = json.dumps({
    "collection": "bikes",
    "database": "rental_bikes",
    "dataSource": "SANDBOXX",
    "filter": {
        "type": '55555'
    },
    "upsert": False,
    "update": {
          "$set": {
              "Status": "non-broke",
              "Since":  "Insert date" 
          }
      }
    })
    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'jNdMKZt2JmBwtYFJSwB8iRRx7M7OVqk0d1fPLuzaMDpLCkWOG7V5jgClzEYUKfV7', 
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)

    result = json.loads(response.text)
    print(result)
    assert isinstance(result, dict)
    
    value = list(result.values())
    
    if result['modifiedCount'] == 1 and result['matchedCount'] == 1:
      print('this file has been update')
      return True
    if result['matchedCount'] == 0 and result['modifiedCount'] == 0:
      print('no matches for this file')
      return False



    return result



if __name__ == "__main__": 
  updateOne()
 