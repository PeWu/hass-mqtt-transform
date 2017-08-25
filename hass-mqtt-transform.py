#!/usr/bin/python3

import json
import paho.mqtt.client as mqtt

# TODO: Convert to command-line flags.
MQTT_HOST = "localhost"
MQTT_PORT = 1883
EVENTSTREAM_TOPIC = "ha/events"
STATE_TOPIC_PREFIX = "ha/states/"


def onConnect(client, userdata, flags, rc):
  print("Connected with result code " + str(rc))
  client.subscribe(EVENTSTREAM_TOPIC)


def onMessage(client, userdata, message):
  payload = json.loads(message.payload.decode('utf-8'))
  eventType = payload["event_type"]
  if eventType == "state_changed":
    eventData = payload["event_data"]
    entityId = eventData["entity_id"]
    newState = eventData["new_state"]
    client.publish(
        STATE_TOPIC_PREFIX + entityId, json.dumps(newState), retain = True)


client = mqtt.Client()
client.on_connect = onConnect
client.on_message = onMessage

client.connect(MQTT_HOST, MQTT_PORT, 60)
client.loop_forever()
