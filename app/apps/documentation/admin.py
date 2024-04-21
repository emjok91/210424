```python
from django.contrib import admin
from .models import Documentation

@admin.register(Documentation)
class DocumentationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')
```