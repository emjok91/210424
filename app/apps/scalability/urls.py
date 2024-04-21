```python
from django.urls import path
from . import views

urlpatterns = [
    path('monitor/', views.monitor_system, name='monitor_system'),
    path('optimize/', views.optimize_system, name='optimize_system'),
]
```