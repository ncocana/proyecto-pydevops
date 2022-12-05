import requests
import json

def insertBike():
  
  url = "https://data.mongodb-api.com/app/data-nxnpm/endpoint/data/v1/action/insertOne"
      
  payload = json.dumps({
    "collection": "bikes",
    "database": "rental_bikes",
    "dataSource": "SANDBOXX",
    "document": {
                 "type":"insert bike name",
                 "mark":"insert mark",
                 "characteristics":{"min_age":{"$numberInt":"0"},
                                    "for_kids?":False,
                                    "bike_capacity":{"$numberInt":"0"},
                                    "number_of_speeds":{"$numberInt":"0"},
                                    "color_bike":["insert_colors"],
                                    "electric_bike?":False,
                                    "characteristics_electric_bike":{"speed":False,
                                                                     "battery_duration_per_km":False,
                                                                     "material_of_battery":False},
                                    "maker_information":{"size of square":[{"$numberInt":"0"},
                                                                           {"$numberInt":"0"}],
                                                         "material_of_bike":"titanium",
                                                         "development":"2x15",
                                                         "maker":"ace group"},
                                    "acessories":["ring bell","mobile support"]},
                 "avalaibility":True,
                 "units_in_shop":{"$numberInt":"0"},
                 "price_of_rent_per_hour":{"$numberDecimal":"0.0"},
                 "price_of_broke":{"$numberDecimal":"0.0"}}
  })
  headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': 'jNdMKZt2JmBwtYFJSwB8iRRx7M7OVqk0d1fPLuzaMDpLCkWOG7V5jgClzEYUKfV7', 
  }
  
  response = requests.request("POST", url, headers=headers, data=payload)
  
  result = json.loads(response.text)
  
  assert isinstance(result, dict)

  return result

if __name__ =='__main__':
  
  insertBike()
  