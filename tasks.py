from time import sleep
from celery import Celery

app = Celery('tasks', broker='amqp://', backend='redis://')


@app.task(bind=True)
def bigtask(self):
    for i in range(30):
        self.update_state(state='RUNNING', meta={'current': i+1})
        sleep(1)
    return "Finished successfully!"
