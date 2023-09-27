# import requests
#
# SHEETY_ENDPOINT = "https://api.sheety.co/7841abbd283b105c897f80243e2cbdf2/flightDeals/prices"
#
# location_dict = {}
#
# g_response = requests.get(url=SHEETY_ENDPOINT)
# locations = g_response.json()['prices']
#
# for location in locations:
#
#     location_dict[location["id"]] = location['city']
#

# kiwi_endpoint = "https://api.tequila.kiwi.com/locations/query"
#
# kiwi_header = {
#     'apikey' : 's-fNH6m3T1BZCVYogaJ5gqMYTOlXM3Uu',
#     'accept' : 'application/json'
# }
#
# kiwi_params = {
#     'term' : "",
#     'locale': "en-US",
#     'location_types': 'airport',
#     "active_only" : "true"
# }
#
# g_sheet_data = {
#
#   "price": {
#         'iataCode' : ""
#   }
# }
#
# for key,value in location_dict.items():
#
#     SHEETY_ENDPOINT_TEMP = SHEETY_ENDPOINT + f'/{key}'
#
#     kiwi_params['term'] = value
#
#     kiwi_response = requests.get(url=kiwi_endpoint,params=kiwi_params,headers=kiwi_header)
#
#     IATA_CODE = kiwi_response.json()['locations'][0]['id']
#
#     g_sheet_data['price']['iataCode'] = IATA_CODE
#
#     response = requests.put(url=SHEETY_ENDPOINT_TEMP, json=g_sheet_data)
#
