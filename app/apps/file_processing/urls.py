```python
from django.urls import path
from . import views

urlpatterns = [
    path('process/', views.process_file, name='process_file'),
]
```