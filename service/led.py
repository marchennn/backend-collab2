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
    async def control_led(status: str) -> ResultLED:
        """
        Mengontrol LED dengan mengirim pesan MQTT dan memperbarui database.
        """
        print("test 1")
        # # Validasi LED ID
        # if led_id not in ["1", "2", "3", "4", "5"]:
        #     raise HTTPException(status_code=400, detail="Invalid LED ID. LED ID must be 1, 2, 3, or 4.")

        # Validasi status
        if status.lower() not in ["on", "off"]:
            raise HTTPException(status_code=400, detail="Invalid status. Status must be 'on' or 'off'.")

        # Publish pesan ke MQTT menggunakan aiomqtt
        try:
            async with Client(MQTT_BROKER, MQTT_PORT) as client:
                topic = "led/1"  # Topik MQTT untuk LED tertentu  
                payload = json.dumps({"led1": status.lower()})  # Format pesan yang akan dikirim
                await client.publish(topic, payload)  # Publish ke MQTT
                print("test")
        except MqttError as e:
            raise HTTPException(status_code=500, detail=f"Failed to publish MQTT message: {str(e)}")

        # Update status dan PWM di database
        try:
            updated_led = await DBLed.update_led(status)
            return updated_led
        except:
            print("err")
            raise HTTPException(sts.HTTP_400_BAD_REQUEST)