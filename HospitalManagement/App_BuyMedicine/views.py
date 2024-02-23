from django.shortcuts import render, redirect
from .forms import PatientIDForm
from .models import Patient

def checkPatient(request):
    if request.method == 'POST':
        form = PatientIDForm(request.POST)
        if form.is_valid():
            patient_id = form.cleaned_data['patient_id']
            try:
                patient = Patient.objects.get(patientId=patient_id)
                return redirect('patient_dashboard', patient_id=patient_id)
            except Patient.DoesNotExist:
                return render(request, 'invalidPatient.html')
    else:
        form = PatientIDForm()
    return render(request, 'checkPatient.html', {'form': form})

def patientDashboard(request, patient_id):
    try:
        patient = Patient.objects.get(patientId=patient_id)
        return render(request, 'patientDash.html', {'patient_id': patient_id})
    except Patient.DoesNotExist:
        return render(request, 'invalidPatient.html')
