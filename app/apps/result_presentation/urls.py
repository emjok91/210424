```python
from django.urls import path
from . import views

app_name = 'result_presentation'

urlpatterns = [
    path('processed_files/', views.ProcessedFileList.as_view(), name='processed_files'),
    path('processed_files/<int:pk>/', views.ProcessedFileDetail.as_view(), name='processed_file_detail'),
]
```