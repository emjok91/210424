```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ErrorLog
from .serializers import ErrorLogSerializer

class ErrorLogView(APIView):
    """
    API endpoint that allows errors to be viewed.
    """
    def get(self, request, format=None):
        error_logs = ErrorLog.objects.all()
        serializer = ErrorLogSerializer(error_logs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ErrorLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```