from prisma import Prisma

class DBConnector:
    def __init__(self):
        self.db = Prisma()

    async def connect(self):
        await self.db.connect()

    async def disconnect(self):
        await self.db.disconnect()

db_connector = DBConnector()