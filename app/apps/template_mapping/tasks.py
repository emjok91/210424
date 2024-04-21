```python
from celery import shared_task
from .models import TemplateMapping
from app.apps.task_extraction.models import ExtractedTask

@shared_task
def map_task_to_template(task_id):
    try:
        task = ExtractedTask.objects.get(id=task_id)
        template_mapping = TemplateMapping.objects.get(task_type=task.task_type)
        task.template = template_mapping.template
        task.save()
        return {"status": "success", "message": "Task mapped to template successfully."}
    except ExtractedTask.DoesNotExist:
        return {"status": "error", "message": "Task not found."}
    except TemplateMapping.DoesNotExist:
        return {"status": "error", "message": "No template mapping found for this task type."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
```