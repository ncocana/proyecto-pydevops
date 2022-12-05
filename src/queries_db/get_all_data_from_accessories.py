import requests
import json

def get_all_data_from_accessories():
    url = "https://data.mongodb-api.com/app/data-nxnpm/endpoint/data/v1/action/find"

    payload = json.dumps({
        "collection": "accessories",
        "database": "rental_bikes",
        "dataSource": "SANDBOXX"
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
    for document in get_all_data_from_accessories()['documents']:
        try:
            print(document['description']['color'], '-', document['description']['material'], '-', document['description']['features'], '-', document['description']['size'])        
        
        except KeyError:
            print("One of the field specified is not present on the document's collection. Try another document or field.")
            