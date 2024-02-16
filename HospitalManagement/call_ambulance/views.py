# call_ambulance/views.py
"""
Django View
-------------

This module defines Django Views for call_ambulance
"""
from django.shortcuts import render, redirect
from .models import AmbulanceCall, Hospital
from django.contrib import messages

def ambulance_call_form(request):
    """
    Render the form for calling an ambulance.

    Retrieves a list of hospitals from the database and renders the form template.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Rendered HTML response with the form.
    """
    hospitals = Hospital.objects.all()
    return render(request, 'call_ambulance/call_ambulance_form.html', {'hospitals': hospitals})

def ambulance_dispatch(request):
    """
    Handle the form submission to dispatch an ambulance.

    If the request method is POST, it processes the form data, performs validation,
    and creates a new AmbulanceCall instance. If successful, redirects to a success page;
    otherwise, displays an error message.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Redirects to success page or the call form.
    """
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        hospital_id = request.POST.get('hospital')
        phone_number = request.POST.get('phone_number')

        try:
            ambulance_call = AmbulanceCall.objects.create(
                patient_name=patient_name,
                hospital_id=hospital_id,
                phone_number=phone_number,
            )
            messages.success(request, 'Ambulance dispatched successfully!')
            return redirect('call_ambulance:dispatch_success')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')

    return redirect('call_ambulance:call_form')
