# make_appointment/views.py
from django.shortcuts import render, redirect
from .models import Patient, Appointment
from .forms import AppointmentForm

def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')
    else:
        form = AppointmentForm()

    return render(request, 'make_appointment/make_appointment.html', {'form': form})

def appointment_success(request):
    return render(request, 'make_appointment/appointment_success.html')
