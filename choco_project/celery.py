import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "choco_project.settings")

app = Celery('choco_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task
def update_db():
	from myapi.services.updater import Updater
	u = Updater()
	u.update_products()


app.conf.beat_schedule = {
	"see-you-in-ten-seconds-task": {
		"task": "celery.update_db",
		"schedule": 30.0
	}
}
