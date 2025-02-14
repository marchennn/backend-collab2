from config.database import db_connector
from model.led import ResultLED
from typing import List, Optional

class DBLed:
    @staticmethod
    async def get_led() -> List[ResultLED]:
        return await db_connector.db.led.find_many()
    
    @staticmethod
    async def update_led(led_id:int, status:str) -> ResultLED:
        return await db_connector.db.led.update(    
            where = {"id": led_id},
            data = {"led1": status},
        )