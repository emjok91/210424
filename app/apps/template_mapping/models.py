```python
from django.db import models

class Template(models.Model):
    name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)

class TaskTemplateMapping(models.Model):
    task_type = models.CharField(max_length=255)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
```