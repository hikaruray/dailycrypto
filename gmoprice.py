import requests
import json

# ----------------------------------
# GET COIN PRICE FROM GMO COINS
# ----------------------------------

endPoint = 'https://api.coin.z.com/public'
path     = '/v1/ticker'

response = requests.get(endPoint + path)

data = response.json()

new = data['data']
currencyName = new[4]['symbol']
price1 = new[4]['ask']
currencyName2 = new[3]['symbol']
price2 = new[3]['ask']

print(f"The price of {currencyName} is {price1}yen\nThe price of {currencyName2} is {price2}yen")
# The price of XRP is 150.528yen
# The price of LTC is 24062yen