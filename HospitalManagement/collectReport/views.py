# collectReport/views.py
from django.shortcuts import render, redirect
from .forms import PatientReportForm

def submitReport(request):
    if request.method == 'POST':
        form = PatientReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Add a URL name for the success page
    else:
        form = PatientReportForm()

    return render(request, 'collect_report_form.html', {'form': form})
