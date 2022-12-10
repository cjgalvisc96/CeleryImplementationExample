from celery import Celery

from src import celeryconfig
from src.config import app_settings

celery_app = Celery(app_settings.CELERY_APP_NAME)
celery_app.config_from_object(celeryconfig)


@celery_app.task()
def simple_implementation_task(*, name: str):
    print("*" * 20)
    print(f"Hello {name}")
    print("*" * 20)
