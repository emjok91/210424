```python
from django.urls import path
from . import views

app_name = 'error_handling'

urlpatterns = [
    path('log/', views.LogErrorView.as_view(), name='log_error'),
]
```