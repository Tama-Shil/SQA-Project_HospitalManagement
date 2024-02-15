"""
Module: views

This module contains view functions for rendering different pages.

"""

from django.shortcuts import render

def home(request):
    """
    Renders the homepage.

    Args:
        request: HttpRequest object.

    Returns:
        HttpResponse: Rendered homepage HTML page.
    """
    return render(request, 'homepage.html')
