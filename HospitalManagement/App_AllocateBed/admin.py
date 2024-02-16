from django.contrib import admin
from .models import Bed, Patient
class BedAdmin(admin.ModelAdmin):
    """
    Customizes the Bed admin interface.

    Allows for better management of Bed instances in the Django admin.
    """
    pass

class PatientAdmin(admin.ModelAdmin):
    """
    Customizes the Patient admin interface.

    Allows for better management of Patient instances in the Django admin.
    """
    pass

admin.site.register(Bed)

admin.site.register(Patient)
