from pydantic import BaseModel
from prisma.models import sensor

class DataSensor(BaseModel):
    temperature:float
    humidity:float
    jarak:float
    jarak2:float

ResultSensor = sensor

