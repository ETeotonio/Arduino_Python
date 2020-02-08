import requests
import settings

def set_led_status_ethernet(message):
    arduino_ip,arduino_port = settings.config_parser('config.ini','Arduino')
    url = 'http://{}:{}/setLedStatus?param={}'.format(arduino_ip,arduino_port,message)
    response = requests.get(url)
    return response.json()
