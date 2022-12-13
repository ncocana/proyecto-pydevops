#To succesfuslly invoke the variables inside the file 'DataAPIKey.py', as it is in another folder,
#we need to specify its path with 'sys'. And then it is possible to call it.
from sys import path as systemPath
systemPath.insert(0, './')
from DataAPIKey import *
import requests
import json

def get_bikes_by_characteristics(char1='', char2='', char3=''):
    
    url = "https://data.mongodb-api.com/app/data-ivdit/endpoint/data/v1/action/find"

    global payload
    print(char1,char2,char3)
    if char1 != "" and char2 == "" and char3 == "":
        payload = json.dumps({
        "collection": "bikes",
        "database": "rental_bikes",
        "dataSource": "Sandbox",
        "filter": {"characteristics.acessories":{"$all":[char1]}}
        })
    elif char1 != "" and char2 != "" and char3 == "":
        payload = json.dumps({
        "collection": "bikes",
        "database": "rental_bikes",
        "dataSource": "Sandbox",
        "filter": {"characteristics.acessories":{"$all":[char1, char2]}}
        })
    else:
        payload = json.dumps({
        "collection": "bikes",
        "database": "rental_bikes",
        "dataSource": "Sandbox",
        "filter": {"characteristics.acessories":{"$all":[char1, char2, char3]}}
        })

    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': APIKey, 
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    result = json.loads(response.text)

    return result

if __name__ == "__main__":

    #Tests if it gets KeyError or not inside a "for in".
    for document in get_bikes_by_characteristics('potentiometer')['documents']:
        try:
            print('It has one characteristic:', document['type'], '-', document['avalaibility'], '-', document['characteristics']['acessories'])
        except KeyError:
            print("One of the field specified is not present on the document's collection. Try another document or field.")
            continue

    #Tests if it gets KeyError or not inside a "for in".
    for document in get_bikes_by_characteristics('back emergency light', 'frontal_light')['documents']:
        try:
            print('It has two characteristics:', document['type'], '-', document['avalaibility'], '-', document['characteristics']['acessories'])
        except KeyError:
            print("One of the field specified is not present on the document's collection. Try another document or field.")
            continue
    
    #Tests if it gets KeyError or not inside a "for in".
    for document in get_bikes_by_characteristics("helmet", "ring bell", "mobile support")['documents']:
        try:
            print('It has three characteristics:', document['type'], '-', document['avalaibility'], '-', document['characteristics']['acessories'])
        except KeyError:
            print("One of the field specified is not present on the document's collection. Try another document or field.")
            continue

    #print(get_bikes_by_characteristics("helmet", "ring bell", "mobile support"))