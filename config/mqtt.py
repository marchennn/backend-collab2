import aiomqtt
from config import Config
import asyncio

class MQTTClient:
    def __init__(self):
        self.broker = Config.MQTT_BROKER
        self.port = Config.MQTT_PORT
        self.topic = Config.MQTT_TOPIC

    async def listen(self):
        async with aiomqtt.Client(hostname=self.broker, port=self.port) as client:
            await client.subscribe(self.topic)
            async for message in client.messages:
                payload = message.payload.decode()
                print(f"Received: {payload}")
                await self.handle_message(payload)

    async def handle_message(self, payload):
        print(f"Handling message: {payload}")

mqtt_client = MQTTClient()