import json
from repository.led import DBLed
from model.led import ResultLED
from typing import List
from aiomqtt import Client, MqttError
from fastapi import HTTPException, status as sts

# Konfigurasi MQTT broker
MQTT_BROKER = "192.168.0.106"  # Ganti dengan alamat broker MQTT Anda
MQTT_PORT = 1883


class LED:
    @staticmethod
    async def get_led() -> List[ResultLED]:
        return await DBLed.get_led()
    
    @staticmethod
    async def control_led(led_id: int, status1: str, status2: str, status3: str, status4: str, status5: str) -> ResultLED:
        statuses = [status1, status2, status3, status4, status5]
        for i, status in enumerate(statuses, start=1):
            if status not in ["on", "off"]:
                raise HTTPException(sts.HTTP_400_BAD_REQUEST, detail="invalid status for LED {i}.")

        # Publish pesan ke MQTT menggunakan aiomqtt
        try:
            async with Client(MQTT_BROKER, MQTT_PORT) as client:
                for i, status in enumerate(statuses, start=1):
                    topic = f"led/{i}"
                    payload = json.dumps({"status": status})  # Format pesan yang akan dikirim
                    await client.publish(topic, payload)  # Publish ke MQTT
        except MqttError as e:
            raise HTTPException(status_code=500, detail=f"Failed to publish MQTT message: {str(e)}")

        # Update status dan PWM di database
        try:
            updated_led = await DBLed.update_led(statuses)
            return updated_led
        except:
            print("err")
            raise HTTPException(sts.HTTP_400_BAD_REQUEST)