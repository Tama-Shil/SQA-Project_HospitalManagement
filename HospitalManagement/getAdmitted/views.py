from django.shortcuts import render,redirect

# Create your views here.
def form_page(request):
    return render(request,'patient_admission_form.html')