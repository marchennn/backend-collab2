import uvicorn
from fastapi import FastAPI
from config import Config
from controller.sensor import router_sensor
from controller.led import router_led

app = FastAPI()
class Server:
    def begin(self):
        app.include_router(router_sensor, prefix="/api/sensor", tags=["Data Sensor & LED"])
        app.include_router(router_led, prefix="/api/led")
        config = uvicorn.Config(app,Config.SERVER_HOST,Config.SERVER_PORT)
        self.__server = uvicorn.Server(config)

    async def start(self):
        await self.__server.serve()

    async def stop(self):
        await self.__server.shutdown()