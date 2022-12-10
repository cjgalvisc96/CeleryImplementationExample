from src.config import app_settings

# imports = ("tasks.simple_implementation_task",)

broker_url = app_settings.RABBITMQ_URI


task_serializer = app_settings.CELERY_TASK_SERIALIZER
result_serializer = app_settings.CELERY_RESULT_SERIALIZER

result_backend = f"{app_settings.MONGO_URI}/"
mongodb_backend_settings = {
    "database": app_settings.MONGO_DB,
    "taskmeta_collection": app_settings.CELERY_TASKMETA_COLLECTION,
}
