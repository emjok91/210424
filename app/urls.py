```python
from django.urls import path, include

urlpatterns = [
    path('file_upload/', include('app.apps.file_upload.urls')),
    path('file_processing/', include('app.apps.file_processing.urls')),
    path('task_extraction/', include('app.apps.task_extraction.urls')),
    path('template_mapping/', include('app.apps.template_mapping.urls')),
    path('template_filling/', include('app.apps.template_filling.urls')),
    path('result_presentation/', include('app.apps.result_presentation.urls')),
    path('error_handling/', include('app.apps.error_handling.urls')),
    path('security/', include('app.apps.security.urls')),
    path('scalability/', include('app.apps.scalability.urls')),
    path('documentation/', include('app.apps.documentation.urls')),
]
```