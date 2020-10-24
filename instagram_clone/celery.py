import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
# IMPORTANT check the name of your project and replace it here 'yourproject.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'instagram_clone.settings')

# IMPORTANT check the name of your project and replace it here 'yourproject'
app = Celery('instagram_clone')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')