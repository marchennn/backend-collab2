from pydantic import BaseModel
from prisma.models import led

class DataLED(BaseModel):
    led_id: int
    led1:str
    led2:str
    led3:str
    led4:str
    led5:str

ResultLED = led