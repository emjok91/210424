```python
from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'file_id', 'task_type', 'task_details', 'created_at', 'updated_at']
    search_fields = ['task_type', 'task_details']
    list_filter = ['task_type', 'created_at', 'updated_at']

admin.site.register(Task, TaskAdmin)
```