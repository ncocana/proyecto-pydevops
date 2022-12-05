import requests
import json

def count_bikes_by_mark():
    url = "https://data.mongodb-api.com/app/data-nxnpm/endpoint/data/v1/action/aggregate"

    payload = json.dumps({
        "collection": "bikes",
        "database": "rental_bikes",
        "dataSource": "SANDBOXX",
        "pipeline": [{"$group": {"_id": "$type", "count": {"$sum":1}}},
                    { "$sort": { "count": 1 } }]
    })

    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'Z7t903XSzDIf0i7ZihPH1neAng5qGsWBKGYpKjB4gzlDwdwbbq7KtAoeG92y1VF5', 
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    result = json.loads(response.text)

    return result

if __name__ == "__main__":

    #Tests if it gets KeyError or not inside a "for in".
    for document in count_bikes_by_mark()['documents']:
        try:
            print(document['_id'], '-', document['count'])
        except KeyError:
            print("One of the field specified is not present on the document's collection. Try another document or field.")
            continue
