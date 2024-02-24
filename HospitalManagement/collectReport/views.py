# collectReport/views.py
from django.shortcuts import render

def collectReport(request):
    """
    Render the patient report collection form page.

    This view renders the 'collect_report_form.html' template, displaying the
    form page for users to enter patient report information.
    """
    return render(request, 'collect_report_form.html')


def reportNotFound(request):
    """
    Render the page for reporting that the patient's report is not found.

    This view renders the 'report_absent.html' template, displaying information
    about why the report might not be found and providing a way to navigate back.
    """
    return render(request, 'report_absent.html')




#class CollectReportView(View):
    #template_name = 'collect_report_form.html'

   
    #def get(self, request, *args, **kwargs):
       #form = Report()
       #return render(request, self.template_name, {'form': form})

    #def post(self, request, *args, **kwargs):
        #form = Report(request.POST)
        #if form.is_valid():
        #    patient = form.save()
        #    return render(request, 'report_template.html', {'patient': patient})
        #else:
        #   return render(request, 'report_absent.html')
                          
