from config.server import Server
from config.database import db_connector
import asyncio

async def main():
    server = Server()

    server.begin()
    try:
        await server.start()
    finally:
        await db_connector.disconnect()

asyncio.run(main())

