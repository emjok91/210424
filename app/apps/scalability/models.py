```python
from django.db import models

class PerformanceMetrics(models.Model):
    file_id = models.CharField(max_length=255, unique=True)
    upload_time = models.DateTimeField(auto_now_add=True)
    processing_time = models.DurationField()
    extraction_time = models.DurationField()
    mapping_time = models.DurationField()
    filling_time = models.DurationField()
    total_time = models.DurationField()

    class Meta:
        verbose_name_plural = "Performance Metrics"

    def __str__(self):
        return self.file_id
```