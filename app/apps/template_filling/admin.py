```python
from django.contrib import admin
from .models import TemplateFilling

@admin.register(TemplateFilling)
class TemplateFillingAdmin(admin.ModelAdmin):
    list_display = ('id', 'original_file', 'filled_template', 'created_at', 'updated_at')
    search_fields = ('original_file',)
    list_filter = ('created_at', 'updated_at',)
```