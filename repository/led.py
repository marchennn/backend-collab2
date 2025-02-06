from config.database import db_connector
from model.led import ResultLED
from typing import List

class DBLed:
    @staticmethod
    async def get_led() -> List[ResultLED]:
        return await db_connector.db.led.find_many()