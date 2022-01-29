import requests
import json
import pprint

# --------------------------------------------------
# # GETS PRICE OF LTC AND XRP FROM COINMARKETCAP
# --------------------------------------------------

url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'


headers = {
  'Accepts': '',
  'X-CMC_PRO_API_KEY':''
}

parameters={
    'symbol': 'XRP,LTC'
}

response=requests.get(url,headers=headers,params=parameters)

data = json.loads(response.text)
# pprint.pprint(data)

xrp_price_now = data['data']['XRP']['quote']['USD']['price']
# print(xrp_price_now)
ltc_now = data['data']['LTC']['quote']['USD']['price']
# print(ltc_now)

post=f'The price of xrp is USD{xrp_price_now:.3f}.\n The price of ltc is USD{ltc_now:.3f}.\n See you in the next post'
# print(post)