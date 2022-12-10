from src.celery_app import celery_app


@celery_app.task()
def simple_implementation_task(*, name: str):
    print("*" * 20)
    print(f"Hello {name}")
    print("*" * 20)
