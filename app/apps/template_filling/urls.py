```python
from django.urls import path
from . import views

urlpatterns = [
    path('fill_template/', views.fill_template, name='fill_template'),
]
```