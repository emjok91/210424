```python
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Task
from .serializers import TaskSerializer
from .tasks import extract_tasks

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def extract(self, request, pk=None):
        task = self.get_object()
        extract_tasks.delay(task.id)
        return Response({'status': 'Task extraction started'})

    @action(detail=True, methods=['get'])
    def status(self, request, pk=None):
        task = self.get_object()
        return Response({'status': task.status, 'result': task.result})
```