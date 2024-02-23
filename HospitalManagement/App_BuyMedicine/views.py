from django.shortcuts import render, redirect
from .forms import PatientIDForm
from .models import Patient, Medicine

def checkPatient(request):
    """
    View function to check if a patient exists in the database.

    If the request method is POST, it checks the submitted patient ID.
    If the patient exists, it redirects to the patient dashboard.
    If the patient does not exist, it renders the invalid patient template.
    If the request method is GET, it renders the patient ID form.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object.
    """
    if request.method == 'POST':
        form = PatientIDForm(request.POST)
        if form.is_valid():
            patient_id = form.cleaned_data['patient_id']
            try:
                patient = Patient.objects.get(patientId=patient_id)
                return redirect('patient_dashboard', patient_id=patient_id)
            except Patient.DoesNotExist:
                return render(request, 'invalidPatient.html')
    else:
        form = PatientIDForm()
    return render(request, 'checkPatient.html', {'form': form})

def patientDashboard(request, patient_id):
    """
    View function to display the patient dashboard.

    Retrieves the patient details and all available medicines from the database.
    Renders the patient dashboard template with the patient details and medicines.

    Args:
        request (HttpRequest): The HTTP request object.
        patient_id (str): The ID of the patient.

    Returns:
        HttpResponse: The HTTP response object.
    """
    try:
        patient = Patient.objects.get(patientId=patient_id)
        medicines = Medicine.objects.all()
        return render(request, 'patientDash.html', {'patient_id': patient_id, 'medicines': medicines})
    except Patient.DoesNotExist:
        return render(request, 'invalidPatient.html')

def submit_selected_medicines(request, patient_id):
    """
    View function to submit selected medicines for a patient.

    Retrieves the patient details from the database.
    Processes the submitted form data to select medicines and calculate the total bill.
    Renders the medicine summary template with the selected medicines and total bill.

    Args:
        request (HttpRequest): The HTTP request object.
        patient_id (str): The ID of the patient.

    Returns:
        HttpResponse: The HTTP response object.
    """
    try:
        patient = Patient.objects.get(patientId=patient_id)
    except Patient.DoesNotExist:
        # Handle the case where the patient does not exist
        return render(request, 'invalidPatient.html')

    if request.method == 'POST':
        selected_medicines = []
        total_bill = 0
        for medicine in Medicine.objects.all():
            quantity_str = request.POST.get(f'quantity_{medicine.id}', '')  # Get the quantity value as a string
            try:
                quantity = int(quantity_str) if quantity_str else 0  # Convert to integer, or use 0 if empty string
                if quantity > 0 and medicine.inStock:
                    selected_medicines.append({'name': medicine.name, 'price': medicine.price, 'quantity': quantity})
                    total_bill += medicine.price * quantity
            except ValueError:
                # Handle the case where the quantity value is not a valid integer
                pass

        return render(request, 'medicineSummary.html', {'patient': patient, 'selected_medicines': selected_medicines, 'total_bill': total_bill})
    else:
        return redirect('patient_dashboard', patient_id=patient_id)

 