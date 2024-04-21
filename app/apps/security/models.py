```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Custom User model with added fields.
    """
    # Add additional fields here as needed
    pass

class FileAccess(models.Model):
    """
    Model to manage file access permissions.
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file_id = models.CharField(max_length=255)
    can_access = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'file_id',)
```
