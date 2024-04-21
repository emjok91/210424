```python
from django.contrib import admin
from .models import TemplateMapping

@admin.register(TemplateMapping)
class TemplateMappingAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_type', 'template_file')
    search_fields = ('task_type',)
    ordering = ('task_type',)
```