from repository.led import DBLed
from model.led import ResultLED
from typing import List

class LED:
    @staticmethod
    async def get_led() -> List[ResultLED]:
        return await DBLed.get_led()