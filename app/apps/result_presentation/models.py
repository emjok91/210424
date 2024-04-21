```python
from django.db import models
from app.apps.file_upload.models import UploadedFile
from app.apps.task_extraction.models import ExtractedTask
from app.apps.template_filling.models import FilledTemplate

class ProcessedFile(models.Model):
    uploaded_file = models.OneToOneField(UploadedFile, on_delete=models.CASCADE, primary_key=True)
    processed_at = models.DateTimeField(auto_now_add=True)

class TaskPresentation(models.Model):
    processed_file = models.ForeignKey(ProcessedFile, on_delete=models.CASCADE)
    extracted_task = models.OneToOneField(ExtractedTask, on_delete=models.CASCADE)
    filled_template = models.OneToOneField(FilledTemplate, on_delete=models.CASCADE)
    presented_at = models.DateTimeField(auto_now_add=True)
```