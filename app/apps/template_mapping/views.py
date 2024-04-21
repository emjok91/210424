```python
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import TemplateMapping
from .serializers import TemplateMappingSerializer
from .tasks import map_template

class TemplateMappingViewSet(viewsets.ModelViewSet):
    queryset = TemplateMapping.objects.all()
    serializer_class = TemplateMappingSerializer

    @action(detail=True, methods=['post'])
    def map(self, request, pk=None):
        template_mapping = self.get_object()
        task_id = map_template.delay(template_mapping.id)
        return Response({'task_id': task_id, 'detail': 'Template mapping started'})

    @action(detail=True, methods=['get'])
    def status(self, request, pk=None):
        template_mapping = self.get_object()
        result = map_template.AsyncResult(template_mapping.task_id)
        return Response({'status': result.status, 'result': result.result})
```