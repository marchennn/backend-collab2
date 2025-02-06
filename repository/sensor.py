from config.database import db_connector
from model.sensor import ResultSensor
from typing import List

class DBSensor:
    @staticmethod
    async def get_sensor() -> List[ResultSensor]:
        return await db_connector.db.sensor.find_many()

