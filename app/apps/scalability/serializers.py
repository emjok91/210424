```python
from rest_framework import serializers
from .models import ScalabilityModel

class ScalabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ScalabilityModel
        fields = '__all__'
```