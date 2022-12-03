import requests
import json

def findOne():
    url = "https://data.mongodb-api.com/app/data-nxnpm/endpoint/data/v1/action/findOne"

    payload = json.dumps({
    "collection": "bikes",
    "database": "rental_bikes",
    "dataSource": "SANDBOXX",
    "filter": {
        "type": 'highway bike'
    }
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
    try:
        print(str(findOne()) + "file found")
    except KeyError:
        print("This field is not found on the document's collection. Try to rewrite the document or fields.")
        pass
    
