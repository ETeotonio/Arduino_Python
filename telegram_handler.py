import json
import requests
import settings

def send_message(message):
    token,bot_chatid = settings.config_parser('telegram.ini')
    url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=' + bot_chatid + '&parse_mode=Markdown&text=' + message
    response = requests.get(url)
    return response.json()


