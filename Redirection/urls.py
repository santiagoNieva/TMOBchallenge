from django.urls import path
from . import views

urlpatterns = [
    path('get_url', views.get_url, name='get_url'),
]