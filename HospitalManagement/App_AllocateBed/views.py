from django.shortcuts import render, redirect
from .models import Bed, Patient
from .forms import BedForm, PatientForm

def home(request):
    all_beds = Bed.objects.all()
    all_patients = Patient.objects.all()

    context = {"all_beds": all_beds, "all_patients": all_patients}
    return render(request, "home.html",context)

def add_bed(request):
    frm = BedForm()

    if request.method=='POST':
        frm = BedForm(request.POST)
        frm.save()
        return redirect(home)
    
    return render(request, "add_bed.html", {'form': frm})

def add_patient(request):
    frm = PatientForm()

    if request.method=='POST':
        frm = PatientForm(request.POST)
        frm.save()
        return redirect(home)
    
    return render(request, "add_patient.html", {'form': frm})
