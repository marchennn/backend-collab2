from pydantic import BaseModel
from prisma.models import led

class DataLED(BaseModel):
    led1:str
    led2:str

ResultLED = led