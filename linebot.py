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

endPoint = 'https://api.coin.z.com/public'
path     = '/v1/ticker'


def main():
    response = requests.get(endPoint + path)
    data = response.json()
    new = data['data']
    currencyName = new[4]['symbol']
    price1 = new[4]['ask']
    currencyName2 = new[11]['symbol']
    price2 = new[11]['ask']

    post=f"The price of {currencyName} is {price1}yen\nThe price of {currencyName2} is {price2}yen"
    USER_ID = info['USER_ID']
    messages = TextSendMessage(text=post)
    line_bot_api.push_message(USER_ID, messages=messages)

if __name__ == "__main__":
    main()

