import aiomqtt
import json
from prisma import Prisma
import asyncio

db = Prisma()

class MQTT:
    def __init__(self, broker_address: str):
        self.broker_address = "192.168.0.109"

    async def process_message(self, topic: str, payload: str):
        try:
            data = json.loads(payload)

            if topic == "sensor/data":
                await db.sensor.create(
                    data={
                        "temperature": str(data.get("temperature", "0")),
                        "humidity": str(data.get("humidity", "0")),
                        "distance1": str(data.get("jarak", "0")),
                        "distance2": str(data.get("jarak2", "0")),
                    }
                )

            elif topic in ["led/1", "led/3", "led/4", "led/5"]:
                led_key = topic.split("/")[1]
                led_value = data.get(f"led{led_key}")
                pwm_led_value = data.get(f"pwmLed{led_key}")

                if led_value not in ["on", "off"]:
                    print(f"Invalid led{led_key} value: {led_value}")
                    return

                if not isinstance(pwm_led_value, (int, float, str)):
                    print(f"Invalid pwmLed{led_key} value: {pwm_led_value}")
                    return

                await db.led.create(
                    data={
                        f"led{led_key}": led_value,  # "on" atau "off"
                        f"pwmled{led_key}": str(pwm_led_value),  # Angka PWM
                    }
                )

            print(f"Data dari {topic} berhasil disimpan")

        except Exception as e:
            print(f"Error menyimpan data dari {topic}: {e}")

    async def subscribe(self):
        topics = ["sensor/data", "led/1", "led/3", "led/4", "led/5"]
        async with aiomqtt.Client(self.broker_address) as client:
            for topic in topics:
                await client.subscribe(topic)
            print(f"Subscribed to topics: {topics}")

            async for message in client.messages:
                topic = message.topic.value
                payload = message.payload.decode()
                print(f"Received on {topic}: {payload}")
                await self.process_message(topic, payload)

    async def publish(self, topic: str, message: str):
        async with aiomqtt.Client(self.broker_address) as client:
            await client.publish(topic, message)
            print(f"Published to {topic}: {message}")

async def main():
    # Inisialisasi database
    await db.connect()

    # Inisialisasi MQTT client
    mqtt_client = MQTT(broker_address="192.168.0.109")

    try:
        # Mulai subscribe ke topik MQTT
        await mqtt_client.subscribe()
    except Exception as e:
        print(f"Error in MQTT: {e}")
    finally:
        # Tutup koneksi database
        await db.disconnect()

asyncio.run(main())