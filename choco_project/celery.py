import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "choco_project.settings")

app = Celery('choco_project')

app.config_from_object('django.conf:settings', namespace='CELERY')


@app.task
def update():
	"""Task that call other tasks ones an hour"""
	update_postgres_task.apply()
	unite_similar_products.apply()
	update_big_query_task.apply()


@app.task
def update_postgres_task():
	"""Task for parsing new products info and putting it to the postgres"""
	from myapi.services.updater import update_postgres
	update_postgres()


@app.task
def unite_similar_products():
	"""Task for uniting similar products into one (inside Postgres)"""
	from myapi.services.updater import unite_similar_products
	unite_similar_products()


@app.task
def update_big_query_task():
	"""Task for updating Big Query database based on postgres"""
	from myapi.services.updater import update_big_query
	update_big_query()
