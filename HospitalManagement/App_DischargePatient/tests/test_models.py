from App_DischargePatient.models import Patient
import pytest

@pytest.mark.django_db
def test_create_patient():
    patient = Patient.objects.create(
        name="John Doe",
        patientId="P001",
        gender="M",
        cabinNo="C001",
        totalBill=1000,
        paymentPaid=False
    )
    assert patient.name == "John Doe"
    assert patient.patientId == "P001"
    assert patient.gender == "M"
    assert patient.cabinNo == "C001"
    assert patient.totalBill == 1000
    assert not patient.paymentPaid
