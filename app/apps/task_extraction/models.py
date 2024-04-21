```python
from django.db import models
from app.apps.file_upload.models import UploadedFile

class ExtractedTask(models.Model):
    file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)
    task_type = models.CharField(max_length=200)
    task_details = models.TextField()

    def __str__(self):
        return f"{self.task_type} from {self.file.file_name}"
```