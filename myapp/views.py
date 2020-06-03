from django.shortcuts import render
from django.http import JsonResponse
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
    task_id = result.id
    redis_instance.set('task_id', task_id)
    return render(request, 'myapp/start.html', {'task_id': task_id})


def status(request):
    return render(request, 'myapp/status.html', {})


def get_status(request):
    task_id = redis_instance.get('task_id')
    result = AsyncResult(task_id)
    if result.info is not None:
        return JsonResponse(result.info)
    else:
        return JsonResponse({})
