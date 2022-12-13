#To succesfuslly invoke the variables inside the file 'DataAPIKey.py', as it is in another folder,
#we need to specify its path with 'sys'. And then it is possible to call it.
from sys import path as systemPath
systemPath.insert(0, './')
from DataAPIKey import *
import requests
import json

def updateOne():

    url = "https://data.mongodb-api.com/app/data-ivdit/endpoint/data/v1/action/updateOne"

    payload = json.dumps({
    "collection": "bikes",
    "database": "rental_bikes",
    "dataSource": "Sandbox",
    "filter": {
        "type": 'urban prueba'
      },
    "upsert": False,
    "update": {
          "$set": {
              "mark":"Ducati corse"
          }
      }
    })
    
    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': APIKey, 
    }
    
    response = requests.request("POST", url, headers=headers, data=payload)

    result = json.loads(response.text)
    
    if result['modifiedCount'] == 1 and result['matchedCount'] == 1:
      print('The document has been updated.')

    if result['matchedCount'] == 0 and result['modifiedCount'] == 0:
      print('There are no matches for this document.')
    
    return result


if __name__ == "__main__":

  updateOne()
 