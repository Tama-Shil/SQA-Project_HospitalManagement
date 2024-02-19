from django.shortcuts import render

# Create your views here.
def conductMedicalTest(request):
    return render(request,'ConductMedicalTest/ConductMedicalTest.html')