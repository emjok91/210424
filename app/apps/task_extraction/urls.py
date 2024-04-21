```python
from django.urls import path
from . import views

app_name = 'task_extraction'

urlpatterns = [
    path('extract/', views.TaskExtractionView.as_view(), name='extract'),
]
```