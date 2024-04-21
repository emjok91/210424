```python
from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.TemplateMappingView.as_view(), name='template_mapping'),
]
```