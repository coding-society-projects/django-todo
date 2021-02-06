from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('complete/<int:id>', views.complete),
    path('about', views.about),
    path('api/tasks', views.api_tasks)
]