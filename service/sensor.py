from repository.sensor import DBSensor
from model.sensor import ResultSensor
from typing import List

class Sensor:
    @staticmethod
    async def get_sensor() -> List[ResultSensor]:
        return await DBSensor.get_sensor()
