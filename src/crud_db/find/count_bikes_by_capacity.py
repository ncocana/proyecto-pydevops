#To succesfuslly invoke the variables inside the file 'DataAPIKey.py', as it is in another folder,
#we need to specify its path with 'sys'. And then it is possible to call it.
from sys import path as systemPath
systemPath.insert(0, './')
from DataAPIKey import *
import requests
import json

def count_bikes_by_capacity():
    url = "https://data.mongodb-api.com/app/data-ivdit/endpoint/data/v1/action/aggregate"

    payload = json.dumps({
        "collection": "bikes",
        "database": "rental_bikes",
        "dataSource": "Sandbox",
        "pipeline": [{"$group": {"_id": "$characteristics.bike_capacity", "count": {"$sum":1}}},
                    { "$sort": { "count": 1 } }]
    })

    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': API_Noa, 
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    result = json.loads(response.text)

    return result

if __name__ == "__main__":

    #Tests if it gets KeyError or not inside a "for in".
    for document in count_bikes_by_capacity()['documents']:
        try:
            print('Capacity for', document['_id'], 'people -', document['count'])
        except KeyError:
            print("One of the field specified is not present on the document's collection. Try another document or field.")
            continue
