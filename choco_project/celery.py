import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "choco_project.settings")

app = Celery('choco_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

# app.autodiscover_tasks()


@app.task
def update_db():
	from myapi.services.updater import update_products
	# from myapi.repository.models import Product
	# Product.objects.all().delete()
	update_products()
