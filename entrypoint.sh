# Run Celery worker
celery -A run.celery worker -l info

# Run Celery beat
celery -A run.celery beat -l info

python3 run.py