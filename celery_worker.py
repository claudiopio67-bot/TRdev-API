from celery import Celery

celery = Celery(
    "trdev",
    broker="redis://localhost:6379/0"
)

@celery.task
def run_task(agent, action, data):
    return {
        "agent": agent,
        "action": action,
        "status": "done"
    }
