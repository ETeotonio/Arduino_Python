import json
import settings
import telegram_handler
import sys
from datetime import datetime

def handler_message(event,context):
    if(event):
        json_data= json.loads(event)
        resp = telegram_handler.send_message(json_data["message"])
        if(resp['ok']):
            print("{\"status\": \"Message Sent\"}")
        else:
            print("{\"status\": \"Messsage Fail\"}")        

a = sys.argv[1]
handler_message(a,'')