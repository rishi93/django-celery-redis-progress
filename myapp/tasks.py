from time import sleep
from celery import task


@task(bind=True)
def bigtask(self):
    for i in range(30):
        self.update_state(state="RUNNING", meta={'current': i+1, 'total': 30})
        sleep(1)
