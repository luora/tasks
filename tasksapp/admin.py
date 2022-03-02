from django.contrib import admin

from tasksapp.models import Task, TaskImage

# Register your models here.

admin.site.register(Task)
admin.site.register(TaskImage)
