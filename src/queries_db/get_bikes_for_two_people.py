import requests
import json

def get_all_bikes():
    url = "https://data.mongodb-api.com/app/data-ivdit/endpoint/data/v1/action/find"

    payload = json.dumps({
    "collection": "bikes",
    "database": "rental_bikes",
    "dataSource": "Sandbox",
    "filter": {"characteristics.bike_capacity":2}
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
    for i in get_all_bikes()['documents']:
        try:
            print(i['type'], '-', i['avalaibility'], '-', i['price_of_rent_per_hour'])
        except KeyError:
            print("One of the field specified is not present on the document's collection. Try another document or field.")
            pass
