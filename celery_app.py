from celery import Celery
from dotenv import load_dotenv
import os

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
REDIS_URL = os.getenv("REDIS_URL")

celery_app = Celery(
    "pokemon",
    broker=REDIS_URL,
    backend=REDIS_URL,
    include=["src.seed"]
)

celery_app.conf.update(
    imports=["src.seed"],
    task_track_started=True,
    result_expires=3600,
    result_persistent=True,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"]
)