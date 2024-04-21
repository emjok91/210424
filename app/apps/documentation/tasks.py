```python
from celery import shared_task
from django.core.management import call_command

@shared_task
def generate_documentation():
    """
    Task to generate the documentation for the backend system.
    """
    call_command('generate_documentation')
```