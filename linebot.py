import json
from linebot import LineBotApi
from linebot.models import TextSendMessage
import requests
import pprint

# -----------------------------------------
# ACCESS TO LINE BOT AND POST EVERYDAY via GITHUB ACTIONS

# -----------------------------------------

file = open('info.json', 'r')
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

url='https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
headers = {
 
}
parameters={
    'symbol': 'XRP,LTC'
}

def main():
    response=requests.get(url,headers=headers,params=parameters)
    data = json.loads(response.text)
    xrp_price_now = data['data']['XRP']['quote']['USD']['price']
    ltc_now = data['data']['LTC']['quote']['USD']['price']
    post=f'The price of xrp is USD{xrp_price_now:.3f}.\n The price of ltc is USD{ltc_now:.3f}.\n See you in the next post'
    USER_ID = info['USER_ID']
    messages = TextSendMessage(text=post)
    line_bot_api.push_message(USER_ID, messages=messages)

if __name__ == "__main__":
    main()

