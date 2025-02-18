from config.database import db_connector
from model.led import ResultLED
from typing import List, Optional

class DBLed:
    @staticmethod
    async def get_led() -> List[ResultLED]:
        return await db_connector.db.led.find_many()
    
    @staticmethod
    async def update_led(led_id: int, status1: str, status2: str, status3: str, status4: str, status5: str) -> ResultLED:
        return await db_connector.db.led.upsert(
            where={"id": led_id},
            data={
                "update": {
                    "led1": status1,
                    "led2": status2,
                    "led3": status3,
                    "led4": status4,
                    "led5": status5
                },
                "create": {
                    "id": led_id,
                    "led1": status1,
                    "led2": status2,
                    "led3": status3,
                    "led4": status4,
                    "led5": status5
                }
            }
        )