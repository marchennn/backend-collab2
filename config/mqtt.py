import paho.mqtt.client as mqtt
from config import Config
import asyncio

mqtt_client = mqtt.Client()

MQTT_BROKER = Config.MQTT_BROKER
MQTT_PORT = Config.MQTT_PORT
MQTT_TOPIC = Config.MQTT_TOPIC

class MQTT:
    async def begin(self):
        def on_connect(client, userdata, flags, rc):
            client.subscribe(MQTT_TOPIC)

        def on_message(client, userdata, msg):
            payload = msg.payload.decode("utf-8")
            asyncio.create_task(save_message(msg.topic, payload))
            asyncio.create_task(broadcast_message(payload))

        mqtt_client.on_connect = on_connect
        mqtt_client.on_message = on_message
        mqtt_client.connect(MQTT_BROKER, MQTT_BROKER, 60)
        mqtt_start = mqtt_client.loop_start()