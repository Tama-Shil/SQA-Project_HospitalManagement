from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """
    Admin class for managing patients in the system.

    :param list_display: A tuple of fields to display in the admin interface.
    :type list_display: tuple
    """
    list_display = ('name', 'patientId', 'gender', 'cabinNo', 'totalBill','paymentPaid' )
