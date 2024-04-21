```python
from rest_framework import serializers
from .models import ErrorLog

class ErrorLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorLog
        fields = ['id', 'timestamp', 'error_type', 'error_message', 'file_id']
```