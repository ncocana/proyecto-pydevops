#To succesfuslly invoke the variables inside the file 'DataAPIKey.py', as it is in another folder,
#we need to specify its path with 'sys'. And then it is possible to call it.
from sys import path as systemPath
systemPath.insert(0, './')
from DataAPIKey import *
import requests
import json

def get_bikes_sorted_by_price():
    url = "https://data.mongodb-api.com/app/data-ivdit/endpoint/data/v1/action/find"

    payload = json.dumps({
    "collection": "bikes",
    "database": "rental_bikes",
    "dataSource": "Sandbox",
    "sort": { "price_of_rent_per_hour": 1 }
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
    for document in get_bikes_sorted_by_price()['documents']:
        try:
            print(document['type'], '-', document['avalaibility'], '-', document['price_of_rent_per_hour'])
        except KeyError:
            print("One of the field specified is not present on the document's collection. Try another document or field.")
            continue

    #Tests if it gets KeyError outside a "for in".
    try:
        print('La más barata es:', get_bikes_sorted_by_price()['documents'][0]['type'], '. Y la más cara es:', get_bikes_sorted_by_price()['documents'][-1]['type'])
    except KeyError:
        print("This field is not present on the document's collection. Try another document or field.")
        pass
