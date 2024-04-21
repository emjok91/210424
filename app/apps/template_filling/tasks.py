```python
from celery import shared_task
from .models import TemplateFilling
from PyPDF2 import PdfFileWriter, PdfFileReader
import re

@shared_task
def fill_template(task_id, template_path, output_path):
    try:
        task = TemplateFilling.objects.get(id=task_id)
        pdf = PdfFileReader(template_path)
        pdf_writer = PdfFileWriter()

        for page in range(pdf.getNumPages()):
            page = pdf.getPage(page)
            content = page.extractText()

            # Replace placeholders with actual data
            for placeholder, value in task.data.items():
                content = re.sub(placeholder, value, content)

            page.setData(content)
            pdf_writer.addPage(page)

        with open(output_path, 'wb') as out:
            pdf_writer.write(out)

        task.status = TemplateFilling.COMPLETED
        task.save()

    except Exception as e:
        task.status = TemplateFilling.FAILED
        task.error_message = str(e)
        task.save()
```
