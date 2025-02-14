from fastapi import APIRouter, HTTPException
from service.led import LED
from model.led import ResultLED
from typing import List

router = APIRouter()

@router.get("/data-led", response_model=List[ResultLED])
async def get_led():
    data = await LED.get_led()
    return data

@router.post("/kontrol-led", response_model=ResultLED)
async def control_led(status: str = None):
    print("test2")
    data = await LED.control_led(status=status)
    return data

router_led = router