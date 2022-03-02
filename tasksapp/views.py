from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from tasksapp.models import Task

from tasksapp.serializers import TaskSerializer

# Create your views here.

class UploadTaskView(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


