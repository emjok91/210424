```python
from celery import shared_task
from .models import ProcessedFile
from django.core.paginator import Paginator

@shared_task
def get_processed_files(page_number=1, items_per_page=10):
    processed_files = ProcessedFile.objects.all().order_by('-processed_at')
    paginator = Paginator(processed_files, items_per_page)
    page = paginator.get_page(page_number)
    return {
        'total_pages': paginator.num_pages,
        'current_page': page_number,
        'items_per_page': items_per_page,
        'results': [{
            'file_id': file.file_id,
            'task_details': file.task_details,
            'template_url': file.template_url,
        } for file in page]
    }

@shared_task
def notify_user(email, message):
    # This is a placeholder for the actual implementation
    # You might want to use Django's EmailMessage class or a third-party service like SendGrid
    pass
```