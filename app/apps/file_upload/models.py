```python
from django.db import models
from django.utils import timezone

class UploadedFile(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.id}'
```