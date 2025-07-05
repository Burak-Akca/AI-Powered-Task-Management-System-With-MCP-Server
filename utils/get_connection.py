import psycopg2
import os
import time
from dotenv import load_dotenv
load_dotenv()

def get_connection(max_wait=30, retry_interval=1):
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    port = os.getenv("DB_PORT")
    dbname = os.getenv("DB_NAME")
    
    connection_url = f"postgresql://{user}:{password}@localhost:{port}/{dbname}"
    connection_url = "postgresql://noter:noterpass@localhost:5432/notedb"
    return psycopg2.connect(connection_url)
