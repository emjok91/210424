```python
from django.contrib import admin
from .models import ScalabilityModel

@admin.register(ScalabilityModel)
class ScalabilityAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at']
    search_fields = ['id']
    list_filter = ['created_at', 'updated_at']
```