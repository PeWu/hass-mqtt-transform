#!/usr/bin/python3

import argparse
import json
import paho.mqtt.client as mqtt
from functools import partial


def onConnect(topics, client, userdata, flags, rc):
  print('Connected with result code ' + str(rc))
  for topic in topics:
    client.subscribe(topic)


def onMessage(prefix, client, userdata, message):
  payload = json.loads(message.payload.decode('utf-8'))
  eventType = payload['event_type']
  if eventType == 'state_changed':
    eventData = payload['event_data']
    entityId = eventData['entity_id']
    newState = eventData['new_state']
    client.publish(prefix + entityId, json.dumps(newState), retain = True)


def main():
  parser = argparse.ArgumentParser(
      description =
          'Transform Home Assistant Eventstream into separate state topics.')
  parser.add_argument(
      '--mqtt_host',
      default = 'localhost',
      metavar = 'HOST',
      help = 'default: localhost')
  parser.add_argument(
      '--mqtt_port',
      type = int,
      default = 1883,
      metavar = 'PORT',
      help = 'default: 1883')
  parser.add_argument(
      '--eventstream_topics',
      required = True,
      nargs = '+',
      metavar = 'TOPIC',
      help = 'topics to listen on')
  parser.add_argument(
    '--state_topic_prefix',
    required = True,
    metavar = 'PREFIX',
    help = 'topic prefix of published states, e.g. ha/states/')
  args = parser.parse_args()

  client = mqtt.Client()
  client.on_connect = partial(onConnect, args.eventstream_topics)
  client.on_message = partial(onMessage, args.state_topic_prefix)

  client.connect(args.mqtt_host, args.mqtt_port, 60)
  client.loop_forever()


if __name__ == "__main__":
  main()
