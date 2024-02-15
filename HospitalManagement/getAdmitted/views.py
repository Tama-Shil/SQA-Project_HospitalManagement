from django.shortcuts import render,redirect
from getAdmitted.models import Patient

# Create your views here.
def formPage(request):
    """
    Render the patient admission form page.

    This view renders the 'patient_admission_form.html' template, displaying the
    form page for users to enter patient admission information.
    """
    return render(request, 'patient_admission_form.html')

def savePatientData(request):
    """
    Handle POST request with patient admission data.

    Extracts data, creates a Patient object, and saves it to the database.
    Renders 'patient_admission_success.html' as a success page.
    """
    if request.method == "POST":
        # Extract patient admission data from the POST request
        name, age, gender, admissionDate, contact, address, symptoms = (
            request.POST.get('name'),
            request.POST.get('age'),
            request.POST.get('gender'),
            request.POST.get('admissionDate'),
            request.POST.get('contact'),
            request.POST.get('address'),
            request.POST.get('symptoms'),
        )

        # Create a new Patient object with the extracted data and save it
        Patient.objects.create(
            name=name,
            age=age,
            gender=gender,
            admissionDate=admissionDate,
            contact=contact,
            address=address,
            symptoms=symptoms
        )

    return render(request, "patient_admission_success.html")

def patientAdmissionSuccess(request):
    """
    Render the success page for patient admission.

    Displays the 'patient_admission_success.html' template to
    indicate successful patient admission.
    """
    return render(request, 'patient_admission_success.html')