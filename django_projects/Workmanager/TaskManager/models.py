from django.db import models

# models.py
from django.db import models

class PdfFile(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    size = models.PositiveIntegerField()
    num_tables = models.PositiveIntegerField()
    num_rows = models.PositiveIntegerField()
    num_columns = models.PositiveIntegerField()

class PdfTable(models.Model):
    pdf_file = models.ForeignKey(PdfFile, on_delete=models.CASCADE)
    # Define fields for table data, e.g., column headers, rows, etc.
