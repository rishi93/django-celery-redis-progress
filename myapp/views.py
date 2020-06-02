from django.shortcuts import render
from .tasks import bigtask
import redis
from django.conf import settings
from celery.result import AsyncResult


redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT)


# Create your views here.
def index(request):
    return render(request, 'myapp/index.html', {})


def start(request):
    result = bigtask.delay()
    redis_instance.set('task_id', result.id)
    return render(request, 'myapp/start.html', {'task_id': str(result.id)})


def status(request):
    result = AsyncResult(redis_instance.get('task_id'))
    return render(
        request,
        'myapp/status.html', 
        {
            'result_id': result.id,
            'result_state': result.state,
            'result_info': result.info
        }
    )
