from django.shortcuts import render,redirect
from getAdmitted.models import Patient

# Create your views here.
def form_page(request):
    return render(request,'patient_admission_form.html')

def savePatientData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        admissionDate = request.POST.get('admissionDate')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        symptoms = request.POST.get('symptoms')
        data = Patient(name = name, age = age, gender = gender, admissionDate = admissionDate, contact = contact, address = address, symptoms = symptoms)
        data.save()
    return render(request,"patient_admission_success.html")

def patient_admission_success(request):
    return render(request, 'patient_admission_success.html')