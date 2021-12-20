Hi,
This is a script that updates the authorized IP on webshare.io in an specified interval for you automatically.
Just run this command to run it on docker:
```
docker run \
--env APIKEY="YOUR_APIKEY" \
--env DELAY="YOUR_DELAY" \
--name webshare-proxy_ip-updater \
luois45/webshare-proxy_ip-updater:latest
```
YOUR_APIKEY: replace it with your apikey https://proxy.webshare.io/userapi/keys
YOUR_DELAY: replace it with the delay in seconds you want the ip to be set to the ip of the docker container.