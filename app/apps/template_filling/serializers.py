```python
from rest_framework import serializers
from .models import TemplateFilling

class TemplateFillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemplateFilling
        fields = ['id', 'original_file', 'template_file', 'filled_template', 'status']

    def create(self, validated_data):
        return TemplateFilling.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.original_file = validated_data.get('original_file', instance.original_file)
        instance.template_file = validated_data.get('template_file', instance.template_file)
        instance.filled_template = validated_data.get('filled_template', instance.filled_template)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
```