```python
from celery import shared_task
from .models import Task
from spacy import load
from spacy.matcher import Matcher

@shared_task
def extract_tasks(file_id, text):
    nlp = load("en_core_sci_sm")
    doc = nlp(text)

    matcher = Matcher(nlp.vocab)
    pattern = [{"LOWER": "prescription"}, {"LOWER": "referral"}, {"LOWER": "follow-up"}]
    matcher.add("TASK_PATTERN", [pattern])

    tasks = []
    matches = matcher(doc)
    for match_id, start, end in matches:
        span = doc[start:end]
        tasks.append(span.text)

    for task in tasks:
        Task.objects.create(file_id=file_id, task=task)

    return f"Tasks extracted for file {file_id}"
```