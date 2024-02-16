from django.shortcuts import render, redirect
from .models import AmbulanceCall  # Import your models as needed
from django.contrib import messages
from .models import Hospital  # Import your models as needed

def ambulance_call_form(request):
    hospitals = Hospital.objects.all()  # Query the hospitals from your database
    return render(request, 'call_ambulance/call_ambulance_form.html', {'hospitals': hospitals})

def ambulance_dispatch(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        hospital_id = request.POST.get('hospital')
        phone_number = request.POST.get('phone_number')

        # Perform validation and handle the form submission, e.g., create a new AmbulanceCall instance
        # This is just a basic example, adapt it according to your model structure and business logic
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
