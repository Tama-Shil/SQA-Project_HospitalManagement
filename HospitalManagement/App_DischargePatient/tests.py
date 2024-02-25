from django.test import TestCase
from .models import Patient
from .views import dischargePatient
from .forms import DischargeForm
class PatientModelTestCase(TestCase):
    def test_patient_creation(self):
        patient = Patient.objects.create(name="John Doe", patientId="P123", gender="M", cabinNo="C001", totalBill=100.00, paymentPaid=True)
        self.assertEqual(patient.name, "John Doe")
        self.assertEqual(patient.patientId, "P123")
        self.assertEqual(patient.gender, "M")
        self.assertEqual(patient.cabinNo, "C001")
        self.assertEqual(patient.totalBill, 100.00)
        self.assertTrue(patient.paymentPaid)

class PatientViewTestCase(TestCase):
    def test_discharge_patient_view(self):
        request = self.client.post('/discharge/', {'patient_id': 'P123'})
        self.assertEqual(request.status_code, 200)  # Assuming successful discharge redirects to a success page

class PatientFormTestCase(TestCase):
    def test_discharge_form(self):
        form_data = {'patientId': 'P123'}
        form = DischargeForm(data=form_data)
        self.assertTrue(form.is_valid())
