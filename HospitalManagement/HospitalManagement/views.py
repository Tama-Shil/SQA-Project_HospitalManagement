# views.py

from django.shortcuts import render

def home(request):
    """
    Render the home page.

    Displays the 'homepage.html' template to provide the home page content.
    """
    return render(request, 'homepage.html')
