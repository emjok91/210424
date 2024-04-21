```python
from celery import shared_task
from .models import UploadedFile
from PyPDF2 import PdfFileReader
import os

@shared_task
def process_uploaded_file(file_id):
    try:
        file_instance = UploadedFile.objects.get(id=file_id)
        file_path = file_instance.file.path

        # Validate the uploaded file to ensure it is a valid PDF document
        try:
            reader = PdfFileReader(file_path)
            if reader.isEncrypted:
                reader.decrypt('')
            info = reader.getDocumentInfo()
        except:
            raise ValueError("Invalid PDF file")

        # Generate a unique identifier for the uploaded file
        unique_id = os.path.basename(file_path)

        # Update the file instance with the unique identifier
        file_instance.unique_id = unique_id
        file_instance.save()

        # Trigger the processing pipeline
        from app.apps.file_processing.tasks import process_file
        process_file.delay(file_id)

    except UploadedFile.DoesNotExist:
        print(f"UploadedFile with id {file_id} does not exist")
```
