```python
from rest_framework import serializers
from .models import TemplateMapping

class TemplateMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateMapping
        fields = ['id', 'task_type', 'template_path']
```