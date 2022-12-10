from src.celery_app import simple_implementation_task

if __name__ == "__main__":
    simple_implementation_task.delay(name="Cris")
