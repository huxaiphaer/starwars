from celery import Celery
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

app = Flask(__name__)

# Add Redis URL configurations for Celery
app.config["CELERY_BROKER_URL"] = "redis://localhost:6379/0"
app.config["CELERY_RESULT_BACKEND"] = "redis://localhost:6379/0"

# Add periodic tasks
celery_beat_schedule = {
    "time_scheduler": {
        "task": "run.paginate_requested_data",
        # Run every second
        "schedule": 30.0,
    }
}

celery = Celery(app.name)

celery.conf.update(
    result_backend=app.config["CELERY_RESULT_BACKEND"],
    broker_url=app.config["CELERY_BROKER_URL"],
    timezone="UTC",
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    beat_schedule=celery_beat_schedule,
)

# secret key
app.secret_key = "huzaifah"

api = Api(app)

# Cross Origin Resource Sharing
CORS(app)
