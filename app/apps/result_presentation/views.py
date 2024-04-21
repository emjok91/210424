```python
from rest_framework import generics, pagination
from rest_framework.response import Response
from .models import ProcessedFile
from .serializers import ProcessedFileSerializer

class ProcessedFilePagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ProcessedFileListView(generics.ListAPIView):
    queryset = ProcessedFile.objects.all()
    serializer_class = ProcessedFileSerializer
    pagination_class = ProcessedFilePagination

    def list(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
```