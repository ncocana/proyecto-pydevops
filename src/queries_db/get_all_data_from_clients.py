import requests
import json

def get_all_data_from_clients():
    url = "https://data.mongodb-api.com/app/data-ivdit/endpoint/data/v1/action/find"

    payload = json.dumps({
        "collection": "clients",
        "database": "rental_bikes",
        "dataSource": "Sandbox"
    })

    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': '6NFpzs43ERy96QMn8io03GXFuUPteyDRDb0cMzBLIe2ya0TOLsu9CzhtMx24hhAZ', 
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    result = json.loads(response.text)

    return result

if __name__ == "__main__":

    #Tests if it gets KeyError or not inside a "for in".
    for document in get_all_data_from_clients()['documents']:
        try:
            print(document['first_name'], '', document['last_name'], '-', document['contact']['email'], '-', document['address']['street_address'], ', ', document['address']['district'])
        except KeyError:
            print("One of the field specified is not present on the document's collection. Try another document or field.")
            pass

    #Tests if it gets KeyError outside a "for in".
    try:
        print(get_all_data_from_clients()['documents'][0]['address']['street_address'])
    except KeyError:
        print("This field is not present on the document's collection. Try another document or field.")
        pass