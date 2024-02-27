"""
Module: medical_test_management

Description:
This module handles the management of medical tests in a hospital management system.
It provides functionalities to conduct medical tests, save test records, and generate
PDF reports containing test record information.

Functions:
    - generatePdf(data): Generates a PDF document containing the provided data.
    - conductMedicalTest(request): Handles the conduct medical test form submission
      and PDF generation.
"""

from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .forms import TestRecordForm
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors  

def generatePdf(data):
    """
    Generates a PDF document containing the provided data.

    Args:
        data (list): List of lists containing data to be displayed in the PDF.

    Returns:
        HttpResponse: HTTP response containing the generated PDF content.
    """
    # Create a buffer for PDF content
    buffer = BytesIO()

    # Create a PDF document
    doc = SimpleDocTemplate(buffer, pagesize=letter)

    # Create a table object
    table = Table(data)

    # Add style to the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    table.setStyle(style)

    # Add the table to the PDF document
    elements = [table]
    doc.build(elements)

    # Get the PDF content from the buffer
    pdf_data = buffer.getvalue()
    buffer.close()

    # Create an HTTP response with PDF content
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="test_record.pdf"'
    response.write(pdf_data)

    return response

def conductMedicalTest(request):
    """
    Handles the conduct medical test form submission and PDF generation.

    If the form submission is valid, saves the test record and generates a PDF
    containing the test record information. Otherwise, renders the conduct
    medical test form.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered HTML response or PDF download response.
    """
    if request.method == 'POST':
        form = TestRecordForm(request.POST)
        if form.is_valid():
            test_record = form.save()
            messages.success(request, 'Test record saved successfully.')

            # Generate PDF with the form data
            data = [
                ['Field', 'Value'],
                ['Patient ID', test_record.patient_id],
                ['Patient Name', test_record.patient_name],
                ['Patient Age', test_record.patient_age],
                ['Referred Doctor', test_record.referred_doctor],
                ['Test Types', ', '.join(test_record.test_types)],
                ['Notes', test_record.test_notes],
            ]
            return generatePdf(data)
    else:
        form = TestRecordForm()

    return render(request, 'ConductMedicalTest/ConductMedicalTest.html', {'form': form})
