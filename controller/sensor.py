from fastapi import APIRouter
from service.sensor import Sensor
from service.led import LED
from model.sensor import ResultSensor
from model.led import ResultLED
from typing import List
    
router = APIRouter()

@router.get("/sensor", response_model=List[ResultSensor])
async def get_sensor():
    data = await Sensor.get_sensor()
    return data

@router.get("/led", response_model=List[ResultLED])
async def get_led():
    data = await LED.get_led()
    return data

router_sensor = router