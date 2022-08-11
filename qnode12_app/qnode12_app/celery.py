import os
from celery import Celery
from dotenv import load_dotenv

# set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qnode12_app.settings')
load_dotenv()

app = Celery('qnode12_app')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
