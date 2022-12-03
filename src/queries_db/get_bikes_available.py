import requests
import json

def get_all_bikes():
    url = "https://data.mongodb-api.com/app/data-ivdit/endpoint/data/v1/action/find"

    payload = json.dumps({
    "collection": "bikes",
    "database": "rental_bikes",
    "dataSource": "Sandbox",
    "filter": {"avalaibility":True},
    "projection": {"_id":0, "type":1, "avalaibility":1, "price_of_rent_per_hour":1}
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
    for i in get_all_bikes()['documents']:
        print(i['type'], '-', i['avalaibility'], '-', i['price_of_rent_per_hour'])
