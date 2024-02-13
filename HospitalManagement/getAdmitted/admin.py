# admin.py
from django.contrib import admin
from .models import Patient  # Import your model

admin.site.register(Patient)  # Register your model with the admin
