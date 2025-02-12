from fastapi import APIRouter, HTTPException
from service.led import LED
from model.led import ResultLED
from typing import List
from config.mqtt import MQTT  # Pastikan MQTT client sudah diinisialisasi di sini
import json

router = APIRouter()

# Inisialisasi MQTT client
mqtt_client = MQTT()

@router.get("/led", response_model=List[ResultLED])
async def get_led():
    data = await LED.get_led()
    return data

@router.post("/led", response_model=List[ResultLED])
async def control_led(status: str):
    # Validasi status
    if status.lower() not in ["on", "off"]:
        raise HTTPException(status_code=400, detail="Invalid status. Status must be 'on' or 'off'.")

    # Publish pesan ke MQTT
    try:
        topic = ["led/1", "led/2", "led/3", "led/4"]  # Sesuaikan dengan topik yang digunakan di MQTT
        payload = json.dumps({"status": status.lower()})  # Format pesan yang akan dikirim
        await mqtt_client.publish(topic, payload)  # Publish ke MQTT
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to publish MQTT message: {str(e)}")

    # Dapatkan data terbaru dari LED setelah mengontrol
    response = await LED.get_led()
    return response