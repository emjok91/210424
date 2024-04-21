```python
from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

User = get_user_model()

@shared_task
def notify_admins_on_critical_error(error_message):
    admins = User.objects.filter(is_staff=True)
    admin_emails = [admin.email for admin in admins]
    send_mail(
        'Critical Error in Medical Document Processing',
        f'An error occurred: {error_message}',
        'admin@medicaldocprocessor.com',
        admin_emails,
        fail_silently=False,
    )

@shared_task
def notify_user_on_processing_complete(user_id):
    user = User.objects.get(id=user_id)
    send_mail(
        'Medical Document Processing Complete',
        'Your medical documents have been processed successfully.',
        'no-reply@medicaldocprocessor.com',
        [user.email],
        fail_silently=False,
    )
```