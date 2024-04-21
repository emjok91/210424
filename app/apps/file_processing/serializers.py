```python
from rest_framework import serializers
from .models import ProcessedFile

class ProcessedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessedFile
        fields = ['id', 'original_file', 'processed_text', 'status', 'created_at', 'updated_at']
```