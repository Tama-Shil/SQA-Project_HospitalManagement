from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TestRecordForm

def conductMedicalTest(request):
    if request.method == 'POST':
        form = TestRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Test record saved successfully.')
            return redirect('conductMedicalTest')  # Redirect to the same page after saving the test record
    else:
        form = TestRecordForm()
    
    return render(request, 'ConductMedicalTest/ConductMedicalTest.html', {'form': form})
