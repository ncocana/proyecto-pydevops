import requests
import json

def get_all_data_from_bikes():
    url = "https://data.mongodb-api.com/app/data-nxnpm/endpoint/data/v1/action/find"
    

    payload = json.dumps({
        "collection": "bikes",
        "database": "rental_bikes",
        "dataSource": "SANDBOXX"
    })

    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': 'jNdMKZt2JmBwtYFJSwB8iRRx7M7OVqk0d1fPLuzaMDpLCkWOG7V5jgClzEYUKfV7', 
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    result = json.loads(response.text)

    return result

if __name__ == "__main__":

    #Tests if it gets KeyError or not inside a "for in".
    for document in get_all_data_from_bikes()['documents']:
        try:
            print(document['type'], '-', document['mark'])
        except KeyError:
            print("One of the field specified is not present on the document's collection. Try another document or field.")
            continue

    #Tests if it gets KeyError outside a "for in".
    try:
        print(get_all_data_from_bikes()['documents'][0]['type'])
    except KeyError:
        print("This field is not present on the document's collection. Try another document or field.")
        pass
        