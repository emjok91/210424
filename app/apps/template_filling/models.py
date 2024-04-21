```python
from django.db import models

class Template(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='templates/')

class FilledTemplate(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    filled_file = models.FileField(upload_to='filled_templates/')
    task = models.ForeignKey('task_extraction.Task', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```