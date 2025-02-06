from pydantic import BaseModel
from prisma.models import sensor

class DataSensor(BaseModel):
    temperature:float
    humidity:float
    distance1:float
    distance2:float

ResultSensor = sensor

