import time
import requests
import logging
import os

apikey = os.environ['APIKEY']
delay = int(os.environ['DELAY'])

while True:
    ip = requests.get("https://api.ipify.org").text
    response = requests.post("https://proxy.webshare.io/api/proxy/config/",
                             json={"authorized_ips": [ip]},
                             headers={"Authorization": apikey})
    logging.warning('Set IP to: ' + ip)
    del ip
    del response
    time.sleep(delay)
