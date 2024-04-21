```python
from django.db import models

class ErrorLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    file_id = models.CharField(max_length=255)
    stage = models.CharField(max_length=255)
    error_message = models.TextField()
    status_code = models.IntegerField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'Error in {self.stage} for file {self.file_id} at {self.timestamp}'
```