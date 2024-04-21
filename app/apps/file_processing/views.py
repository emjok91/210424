```python
from django.http import JsonResponse
from django.views import View
from .tasks import process_file
from .models import ProcessedFile

class FileProcessingView(View):
    def post(self, request, *args, **kwargs):
        file_id = request.POST.get('file_id')
        if not file_id:
            return JsonResponse({'error': 'Missing file_id'}, status=400)

        try:
            file_instance = ProcessedFile.objects.get(id=file_id)
        except ProcessedFile.DoesNotExist:
            return JsonResponse({'error': 'File not found'}, status=404)

        # Trigger the processing pipeline
        process_file.delay(file_id)

        return JsonResponse({'message': 'Processing started'}, status=202)

    def get(self, request, *args, **kwargs):
        file_id = request.GET.get('file_id')
        if not file_id:
            return JsonResponse({'error': 'Missing file_id'}, status=400)

        try:
            file_instance = ProcessedFile.objects.get(id=file_id)
        except ProcessedFile.DoesNotExist:
            return JsonResponse({'error': 'File not found'}, status=404)

        # Return the processing status and result
        return JsonResponse({
            'file_id': file_instance.id,
            'status': file_instance.status,
            'result': file_instance.result
        }, status=200)
```