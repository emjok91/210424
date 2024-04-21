```python
from django.db import models

class ProcessedFile(models.Model):
    file_id = models.CharField(max_length=255, unique=True)
    original_file = models.FileField(upload_to='original_files/')
    processed_text = models.TextField(blank=True, null=True)
    processing_status = models.CharField(max_length=20, default='pending')
    processing_error = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.file_id
```