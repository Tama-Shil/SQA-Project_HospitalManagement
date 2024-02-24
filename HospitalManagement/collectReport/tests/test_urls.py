# collectReport/tests/test_urls.py
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from collectReport.views import collectReport, reportNotFound

class TestUrls(SimpleTestCase):
    """
    Test suite for URL patterns in the collectReport app.
    """

    def testCollectReportUrlResolves(self):
        """
        Test if the URL for collecting a report resolves to the correct view function.
        """
        url = reverse('collectReport')
        self.assertEqual(resolve(url).func, collectReport)

    def testReportNotFoundUrlResolves(self):
        """
        Test if the URL for reporting not found resolves to the correct view function.
        """
        url = reverse('reportNotFound')
        self.assertEqual(resolve(url).func, reportNotFound)
