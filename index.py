from config.server import Server
# from config.mqtt import MQTT
from config.database import db_connector
import asyncio

async def main():
    await db_connector.connect()
    server = Server()
    # mqtt = MQTT()

    server.begin()
    # mqtt.begin()
    try:
        await server.start()
    finally:
        await db_connector.disconnect()

asyncio.run(main())

