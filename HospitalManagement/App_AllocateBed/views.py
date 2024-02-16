from django.shortcuts import render, redirect
from .models import Bed, Patient
from .forms import BedForm, PatientForm

def home(request):
    """
    Render the home page with a list of all beds and patients.

    :param request: HTTP request
    :type request: HttpRequest

    :return: Rendered HTML template with a list of beds and patients
    :rtype: HttpResponse
    """
    all_beds = Bed.objects.all()
    all_patients = Patient.objects.all()

    context = {"all_beds": all_beds, "all_patients": all_patients}
    return render(request, "home.html",context)

def add_bed(request):
    """
    Render a form to add a new bed and handle form submission.

    :param request: HTTP request
    :type request: HttpRequest

    :return: Rendered HTML template with a form to add a new bed
    :rtype: HttpResponse
    """
    frm = BedForm()

    if request.method=='POST':
        frm = BedForm(request.POST)
        frm.save()
        return redirect(home)
    
    return render(request, "add_bed.html", {'form': frm})

def add_patient(request):
    """
    Render a form to add a new patient and handle form submission.

    :param request: HTTP request
    :type request: HttpRequest

    :return: Rendered HTML template with a form to add a new patient
    :rtype: HttpResponse
    """
    frm = PatientForm()

    if request.method=='POST':
        frm = PatientForm(request.POST)
        frm.save()
        return redirect(home)
    
    return render(request, "add_patient.html", {'form': frm})
