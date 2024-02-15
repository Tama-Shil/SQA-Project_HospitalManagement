from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas

import random

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def prescribePatient(request):
    if request.method == 'POST':
        # Get form data
        patient_name = request.POST.get('patientName', '')
        age = request.POST.get('age', '')
        gender = request.POST.get('gender', '')
        symptoms = request.POST.get('symptoms', '')
        diagnosis = request.POST.get('diagnosis', '')
        prescription = request.POST.get('prescription', '')

        # Generate PDF content using ReportLab
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="prescription.pdf"'

        doc = SimpleDocTemplate(response, pagesize=letter)
        styles = getSampleStyleSheet()
        style_normal = styles['Normal']
        style_heading = styles['Heading1']
        style_heading.alignment = 1  # Center alignment for heading

        content = []

        # Add heading with orange color
        orange_color = colors.HexColor('#FFA500')
        content.append(Paragraph("<font color='#FFA500'><b>Prescription</b></font>", style_heading))
        content.append(Spacer(1, 12))

        # Add patient information with orange color
        content.append(Paragraph("<font color='#FFA500'>Patient Name:</font> " + patient_name, style_normal))
        content.append(Paragraph("<font color='#FFA500'>Age:</font> " + age, style_normal))
        content.append(Paragraph("<font color='#FFA500'>Gender:</font> " + gender, style_normal))
        content.append(Spacer(1, 12))

        # Add symptoms, diagnosis, and prescription with orange color
        content.append(Paragraph("<font color='#FFA500'><b>Symptoms:</b></font>", style_normal))
        content.append(Paragraph(symptoms, style_normal))
        content.append(Paragraph("<font color='#FFA500'><b>Diagnosis:</b></font>", style_normal))
        content.append(Paragraph(diagnosis, style_normal))
        content.append(Paragraph("<font color='#FFA500'><b>Prescription:</b></font>", style_normal))
        content.append(Paragraph(prescription, style_normal))

        doc.build(content)
        
        return response
    else:
        return render(request, 'PrescribePatient/prescription_form.html')
