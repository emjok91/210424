```python
from celery import shared_task
from .models import ErrorLog

@shared_task
def log_error(error_message, error_code, file_id):
    """
    A Celery task to log errors encountered during file processing.
    """
    error_log = ErrorLog(
        error_message=error_message,
        error_code=error_code,
        file_id=file_id
    )
    error_log.save()

@shared_task
def notify_admin(error_message, error_code):
    """
    A Celery task to notify administrators of critical errors.
    """
    # Add code here to send an email or other form of notification to the administrators
    pass
```