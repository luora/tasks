
from django import views
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from tasksapp.views import UploadTaskView

router = DefaultRouter()

router.register(r'uploadtask', UploadTaskView)


urlpatterns= [
    path('', include(router.urls))
]

