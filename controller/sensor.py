from fastapi import APIRouter, HTTPException
from service.sensor import Sensor
from model.sensor import ResultSensor
from typing import List
from aiomqtt import Client, MqttError

router = APIRouter()

@router.get("/data-sensor", response_model=List[ResultSensor])
async def get_sensor():
    data = await Sensor.get_sensor()
    return data

router_sensor = router