```python
from django.contrib import admin
from .models import ErrorLog

@admin.register(ErrorLog)
class ErrorLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'error_type', 'error_message', 'timestamp')
    search_fields = ('error_type', 'error_message')
    list_filter = ('timestamp',)
```