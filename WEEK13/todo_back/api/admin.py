from django.contrib import admin
from api.models import Task, TaskList

# Register your models here.

admin.site.register(Task)
@admin.register(TaskList)
class TaskListsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by', )