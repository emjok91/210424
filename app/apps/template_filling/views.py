```python
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import FilledTemplate
from .serializers import FilledTemplateSerializer
from .tasks import fill_template

class FilledTemplateViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for viewing and retrieving FilledTemplate.
    """
    def list(self, request):
        queryset = FilledTemplate.objects.all()
        serializer = FilledTemplateSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = FilledTemplate.objects.all()
        filled_template = get_object_or_404(queryset, pk=pk)
        serializer = FilledTemplateSerializer(filled_template)
        return Response(serializer.data)

    def create(self, request):
        serializer = FilledTemplateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            fill_template.delay(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```