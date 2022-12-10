from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    # Celery
    CELERY_APP_NAME: str
    CELERY_TASKMETA_COLLECTION: str
    CELERY_TASK_SERIALIZER: str
    CELERY_RESULT_SERIALIZER: str
    # Rabbitmq
    RABBITMQ_DEFAULT_USER: Optional[str]
    RABBITMQ_DEFAULT_PASS: Optional[str]
    RABBITMQ_PROTOCOL_PORT: Optional[str]
    RABBITMQ_UI_PORT: Optional[str]
    RABBITMQ_URI: str
    # Mongo
    MONGO_INITDB_ROOT_USERNAME: Optional[str]
    MONGO_INITDB_ROOT_PASSWORD: Optional[str]
    MONGO_PORT: Optional[str]
    MONGO_DB: str
    MONGO_URI: str

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_app_settings() -> Settings:
    return Settings()


app_settings = get_app_settings()
