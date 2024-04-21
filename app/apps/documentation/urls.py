```python
from django.urls import path
from . import views

urlpatterns = [
    path('docs/', views.DocumentationView.as_view(), name='documentation'),
]
```