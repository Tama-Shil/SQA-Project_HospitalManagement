from django.shortcuts import render
from .forms import DischargeForm
from .models import Patient
        
def dischargePatient(request):
    if request.method == 'POST':
        id = request.POST.get('patient_id')

        try:
            print("Attempting to retrieve patient with ID:", id)
            patient = Patient.objects.get(patientId=id)
            print("Patient found:", patient)
            if patient.paymentPaid:
                return render(request, 'patientDetail.html', {'patient': patient})  # Corrected template name
            else:
                return render(request, 'paymentDue.html')
        except Patient.DoesNotExist:
            print("Patient not found with ID:", id)
            return render(request, 'patientNotFound.html')

    return render(request, 'dischargeForm.html', {'form': DischargeForm()})
