# hass-mqtt-transform

A small script that reads the MQTT stream of Home Assistant events and publishes states back to the same MQTT broker but in separate mqtt topics with retain=true

See forum thread at https://community.home-assistant.io/t/home-assistant-at-home-with-online-dashboard

Prerequisite:
```
  sudo pip3 install paho-mqtt
```
Usage example:
```
  ./hass-mqtt-transform.py --eventstream_topics ha/events --state_topic_prefix ha/states/
```

Connects to the local mqtt broker, reads the Home Assistant eventstream from the `ha/events` topic and writes states to individual topics, e.g. `ha/states/sun.sun`, `ha/states/sensor.pws_weather`.
