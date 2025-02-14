import os
from dotenv import load_dotenv

load_dotenv(override=True)

class Config:
    SERVER_HOST=os.getenv("SERVER_HOST","0.0.0.0")
    SERVER_PORT=int(os.getenv("SERVER_PORT","51000"))
    DB_URL=os.getenv("DB_URL","postgresql://gmh:123@localhost:5432/gmh3sensor")