# views.py
import os
import tabula
from django.shortcuts import render, redirect
from .forms import PdfUploadForm
from .models import PdfFile

def upload_pdf(request):
    if request.method == 'POST':
        form = PdfUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']
            # Save the uploaded PDF file
            destination = os.path.join('path_to_save_uploads', pdf_file.name)
            with open(destination, 'wb+') as destination_file:
                for chunk in pdf_file.chunks():
                    destination_file.write(chunk)

            # Process the PDF file using Tabula
            # (You need to install tabula-py: pip install tabula-py)
            tables = tabula.read_pdf(destination, pages='all', multiple_tables=True)
            num_tables = len(tables)

            # Extract metadata
            pdf_size = os.path.getsize(destination)
            pdf_name = pdf_file.name
            # Extract num_rows and num_columns from the tables (customize based on your needs)

            # Store metadata in the database
            pdf = PdfFile(
                name=pdf_name,
                location=destination,
                size=pdf_size,
                num_tables=num_tables,
                num_rows=0,  # Set appropriately based on the extracted table data
                num_columns=0,  # Set appropriately based on the extracted table data
            )
            pdf.save()

            # Redirect to a success page
            return redirect('success_page')  # Define the URL name for the success page

    else:
        form = PdfUploadForm()
    return render(request, 'upload_pdf.html', {'form': form})

def pdf_list(request):
    # Query PDF files and pass them to the template
    pdf_files = PdfFile.objects.all()
    return render(request, 'pdf_list.html', {'pdf_files': pdf_files})
