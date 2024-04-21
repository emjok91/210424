```python
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import long_running_task

class ScalabilityView(APIView):
    def get(self, request):
        # Check if result is in cache
        result = cache.get('long_running_task_result')
        if result is None:
            # If not in cache, execute the task and store the result in cache
            result = long_running_task.delay()
            cache.set('long_running_task_result', result, 60*60*24)  # Cache result for 24 hours
        return Response({"result": result})

    @cache_page(60 * 15)  # Cache this view for 15 minutes
    def get_cached(self, request):
        result = long_running_task.delay()
        return Response({"result": result})

class TaskStatusView(APIView):
    def get(self, request, task_id):
        # Get task status
        task = long_running_task.AsyncResult(task_id)
        response_data = {
            'task_id': task.id,
            'status': task.status,
            'result': task.result,
        }
        return Response(response_data)
```