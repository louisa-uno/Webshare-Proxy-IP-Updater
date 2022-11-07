[![DeepSource](https://deepsource.io/gh/Luois45/Webshare-Proxy-IP-Updater.svg/?label=active+issues&show_trend=true&token=HHmb9l8hZU8dGkK7c19ZxDrc)](https://deepsource.io/gh/Luois45/Webshare-Proxy-IP-Updater/?ref=repository-badge)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)
[![built with: Python3](https://camo.githubusercontent.com/0d9fbff04202da688cc79c5ffe984bd171edf453b2e41e5e56e55202dd5bdbb2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6275696c74253230776974682d507974686f6e332d7265642e737667)](https://www.python.org/)

Hi,<br />
This is a script that updates the authorized IP on webshare.io in an specified interval for you automatically.<br />
Just run this command to run it with docker:
```shell
docker run \
--env APIKEY=YOUR_APIKEY \
--env DELAY=YOUR_DELAY \
--name webshare-proxy_ip-updater \
luois45/webshare-proxy_ip-updater:latest
```
or with docker compose:
```yaml
version: '3.7'
services:
  app:
    image: luois45/webshare-proxy_ip-updater:latest
    environment:
      - APIKEY=YOUR_APIKEY
      - DELAY=YOUR_DELAY
    restart: always
```
**YOUR_APIKEY**: replace it with your apikey https://proxy.webshare.io/userapi/keys<br />
**YOUR_DELAY**: replace it with the delay in seconds you want the ip to be set to the ip of the docker container.
