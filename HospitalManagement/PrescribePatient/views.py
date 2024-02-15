from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas

def prescribePatient(request):
    if request.method == 'POST':
        # Get form data
        patient_name = request.POST.get('patientName', '')
        age = request.POST.get('age', '')
        gender = request.POST.get('gender', '')
        symptoms = request.POST.get('symptoms', '')
        diagnosis = request.POST.get('diagnosis', '')
        prescription = request.POST.get('prescription', '')

        # Generate PDF content using reportlab
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="prescription.pdf"'
        p = canvas.Canvas(response)
        p.setFont("Helvetica", 12)
        p.drawString(100, 800, "Patient Name: " + patient_name)
        p.drawString(100, 780, "Age: " + age)
        p.drawString(100, 760, "Gender: " + gender)
        p.drawString(100, 740, "Symptoms: " + symptoms)
        p.drawString(100, 720, "Diagnosis: " + diagnosis)
        p.drawString(100, 700, "Prescription: " + prescription)
        p.save()
        return response
    else:
        return render(request, 'PrescribePatient/prescription_form.html')
