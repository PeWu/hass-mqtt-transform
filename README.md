# hass-mqtt-transform

A small script that reads the MQTT stream of Home Assistant events and publishes states back to the same MQTT broker but in separate mqtt topics with retain=true

See forum thread at https://community.home-assistant.io/t/home-assistant-at-home-with-online-dashboard

Prerequisite:
```
  sudo pip3 install paho-mqtt
```
