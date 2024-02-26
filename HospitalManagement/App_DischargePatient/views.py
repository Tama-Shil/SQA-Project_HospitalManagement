
from django.shortcuts import render
from .forms import DischargeForm
from .models import Patient

def dischargePatient(request):
    """
    View function to handle patient discharge.

    :param request: HttpRequest object
    :type request: django.http.HttpRequest
    :return: HttpResponse object
    :rtype: django.http.HttpResponse
    """
    if request.method == 'POST':
        id = request.POST.get('patient_id')
        
        try:
            """Attempt to retrieve patient with given ID""" 
            print("Attempting to retrieve patient with ID:", id)
            patient = Patient.objects.get(patientId=id)
            print("Patient found:", patient)
            
            """Check if payment is paid"""
            if patient.paymentPaid:
                return render(request, 'patientDetail.html', {'patient': patient})  # Corrected template name
            else:
                return render(request, 'paymentDue.html')
        except Patient.DoesNotExist:
            """Render patient not found template if patient does not exist"""
            print("Patient not found with ID:", id)
            return render(request, 'patientNotFound.html')

    return render(request, 'dischargeForm.html', {'form': DischargeForm()})

def test_discharge_patient_success(self):
        client = Client()
        url = reverse('discharge_patient')
        
        # Simulate a POST request with the patient ID
        response = client.post(url, {'patient_id': '123'})
        
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check if the correct template is rendered for a discharged patient
        self.assertTemplateUsed(response, 'patientDetail.html')