```python
from django.http import JsonResponse
from django.views import View
from django.core.files.storage import FileSystemStorage
from .tasks import process_file
from .models import UploadedFile
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import uuid

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        if 'file' not in request.data:
            return Response({"file": "No file found in request"}, status=status.HTTP_400_BAD_REQUEST)

        file = request.data['file']
        file_extension = file.name.split('.')[-1]
        if file_extension.lower() != 'pdf':
            return Response({"file": "Invalid file type. Only PDF files are allowed."}, status=status.HTTP_400_BAD_REQUEST)

        unique_id = str(uuid.uuid4())
        file.name = unique_id + '.' + file_extension
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)

        uploaded_file = UploadedFile.objects.create(file_name=filename, file_url=uploaded_file_url, unique_id=unique_id)
        process_file.delay(uploaded_file.id)

        return Response({"file": "File uploaded successfully", "id": unique_id}, status=status.HTTP_201_CREATED)
```