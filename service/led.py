import json
from repository.led import DBLed
from model.led import ResultLED
from typing import List
# from config.mqtt import MQTT

# mqtt_client = MQTT()

class LED:
    @staticmethod
    async def get_led() -> List[ResultLED]:
        return await DBLed.get_led()

    # @staticmethod
    # async def control_led(status: str, pwm: str):
    #     if status.lower() not in ["on", "off"]:
    #         raise HTTPException(status_code=400, detail="Invalid status. Status must be 'on' or 'off'.")

    #     if not (0 <= pwm <= 255):
    #         raise HTTPException(status_code=400, detail="Invalid PWM value. PWM must be between 0 and 255.")

    #     try:
    #         topic = ["led/1", "led/2", "led/3", "led/4"]
    #         payload = json.dumps({"status": status.lower(), "pwm": pwm})
            
    #         for t in topic:
    #             await mqtt_client.publish(t, payload)
                
    #     except Exception as e:
    #         raise HTTPException(status_code=500, detail=f"Failed to publish MQTT message: {str(e)}")
