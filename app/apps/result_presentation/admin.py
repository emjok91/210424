```python
from django.contrib import admin
from .models import ProcessedFile

@admin.register(ProcessedFile)
class ProcessedFileAdmin(admin.ModelAdmin):
    list_display = ('file_id', 'task_details', 'template_url')
    search_fields = ('file_id',)
    ordering = ('file_id',)
```