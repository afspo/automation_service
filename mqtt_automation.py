# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import paho.mqtt.client as mqtt
import json
import pandas as pd
import datetime

# mqtt setup
brokerAddress = '192.168.1.158'
brokerPort = 1883
pyClient = mqtt.Client()
pyClient.connect(brokerAddress, brokerPort)

# Input subscriptions
pyClient.subscribe("zigbee2mqtt/switch_hallway", 0)
pyClient.subscribe("zigbee2mqtt/motion_hallway", 0)
pyClient.subscribe("zigbee2mqtt/ceilingLamp_hallway", 0)

# Create functions
# Hallway switch actuation
def on_message_switch_hallway(pyClient, userdata, message):
    state_switchHallway = pd.read_json(message.payload.decode("UTF-8"))
    if state_switchHallway['action'].iloc[0] == "on":
        pyClient.publish("zigbee2mqtt/ceilingLamp_hallway/set", '{"state":"ON"}')
    else:
        pyClient.publish("zigbee2mqtt/ceilingLamp_hallway/set", '{"state":"OFF"}')

# Hallway motion sensor activation
def on_message_motion_hallway(pyClient, userdata, message):
    state_motionHallway = pd.read_json(message.payload.decode("UTF-8"), typ='series')
    # if state_motionHallway['occupancy'] == 1:
    #     pyClient.publish("zigbee2mqtt/ceilingLamp_hallway/set", '{"state":"ON"}')
    # elif state_motionHallway['occupancy'] == 0:
    #     pyClient.publish("zigbee2mqtt/ceilingLamp_hallway/set", '{"state":"OFF"}')  

while True:
    pyClient.message_callback_add("zigbee2mqtt/switch_hallway", on_message_switch_hallway)
    pyClient.message_callback_add("zigbee2mqtt/motion_hallway", on_message_motion_hallway)
    pyClient.loop_forever()