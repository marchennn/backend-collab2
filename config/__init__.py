import os
from dotenv import load_dotenv

load_dotenv(override=True)

class Config:
    SERVER_HOST=os.getenv("SERVER_HOST","0.0.0.0")
    SERVER_PORT=int(os.getenv("SERVER_PORT","51000"))
    DB_URL=os.getenv("DB_URL", "postgresql://marchen@localhost:5432/mydb")
    MQTT_BROKER=os.getenv("MQTT_BROKER","broker.hivemq.com")
    MQTT_PORT=os.getenv("MQTT_PORT","1883")
    MQTT_TOPIC=os.getenv("MQTT_TOPIC", "sensor/data")