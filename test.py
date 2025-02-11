import asyncio
import aiomqtt
import json
import random

BROKER_URL = "192.168.0.109"
TOPIC = "sensor/data"

async def publish_sensor_data():
    """Mengirimkan data dummy ke topik MQTT"""
    async with aiomqtt.Client(BROKER_URL) as client:
        while True:
            # Membuat data dummy
            sensor_data = {
                "temperature": f"{random.uniform(20, 35):.2f}",
                "humidity": f"{random.uniform(40, 70):.2f}",
                "distance1": f"{random.uniform(5, 20):.2f}",
                "distance2": f"{random.uniform(10, 30):.2f}"
            }
            
            payload = json.dumps(sensor_data)
            await client.publish(TOPIC, payload)
            print(f"Data dikirim: {payload}")

            # Delay 5 detik sebelum mengirim data berikutnya
            await asyncio.sleep(5)

async def main():
    await publish_sensor_data()

asyncio.run(main())
