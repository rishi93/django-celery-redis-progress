from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('start/', views.start, name='start'),
    path('status/', views.status, name='status')
]
