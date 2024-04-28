import time
import requests
import logging
import os

apikey, delay = os.environ['APIKEY'], int(os.environ['DELAY'])
last_ip = ""

while True:
    ip = requests.get("https://api.ipify.org").text
    if ip != last_ip:
        response = requests.post("https://proxy.webshare.io/api/proxy/config/",
                                json={"authorized_ips": [ip]},
                                headers={"Authorization": apikey})
        if response.status_code == 200:
            if response.json()["authorized_ips"][0] == ip:
                logging.warning("Successfully updated ip to: " + ip)
            else:
                logging.warning("Ip didn't update to " + ip + " for some reason")
        else:
            logging.warning("Received " + response.status_code + " error while updating ip to: " + ip)
    last_ip = ip
    time.sleep(delay)