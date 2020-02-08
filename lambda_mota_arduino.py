import json
import settings
import telegram_handler
import sys
import arduino_handler

def handler_message(event,context):
    if(event):
        json_data= json.loads(event)
        resp = telegram_handler.send_message(json_data["message"])
        resp_arduino = arduino_handler.set_led_status_ethernet(json_data["message"])


a = sys.argv[1]
handler_message(a,'')