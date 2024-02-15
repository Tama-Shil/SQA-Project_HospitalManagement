"""
Django View
-------------

This module defines Django Views for App_Payment.
"""

from django.shortcuts import render
from .models import Patient


def selectPaymentMethod(request):
    """
    View for selecting a payment method.
    This view handles both POST and GET requests. If the request method is POST,it retrieves or creates a patient instance based on the provided patient ID.
    Then, it renders the 'payment_success.html' template with the patient data.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :Returns: The HTTP response containing the rendered template.
    :rtype: HttpResponse
    """
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        patient_name = request.POST.get('patient_name')
        # Check if the patient already exists based on the provided patient_id
        # If the patient exists, retrieve the existing instance
        # If not, create a new instance
        patient, created = Patient.objects.get_or_create(patient_id=patient_id, defaults={'patient_name': patient_name})
        
        return render(request, 'payment_success.html', {'patient': patient, 'created': created})
    
    return render(request, 'selectPaymentMethod.html')



def paymentSuccess(request):
    """
    View for displaying payment success.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :Returns: The HTTP response containing the rendered template.
    :rtype: HttpResponse
    """
    patients = Patient.objects.all()
    return render(request, 'payment_successful.html', {'patients': patients})
