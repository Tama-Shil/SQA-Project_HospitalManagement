# collectReport/tests/test_views.py
from django.test import TestCase
from django.urls import reverse


class CollectReportViewTest(TestCase):
    """
    Test suite for the views related to collecting a report.
    """

    def testCollectReportViewStatusCode(self):
        """
        Test if the view for collecting a report returns a 200 status code.
        """
        response = self.client.get(reverse('collectReport'))
        self.assertEqual(response.status_code, 200)

    def testCollectReportViewTemplateUsed(self):
        """
        Test if the correct template is used when rendering the view for collecting a report.
        """
        response = self.client.get(reverse('collectReport'))
        self.assertTemplateUsed(response, 'collect_report_form.html')


class ReportNotFoundViewTest(TestCase):
    """
    Test suite for the views related to reporting not found.
    """

    def testReportNotFoundViewStatusCode(self):
        """
        Test if the view for reporting not found returns a 200 status code.
        """
        response = self.client.get(reverse('reportNotFound'))
        self.assertEqual(response.status_code, 200)

    def testReportNotFoundViewTemplateUsed(self):
        """
        Test if the correct template is used when rendering the view for reporting not found.
        """
        response = self.client.get(reverse('reportNotFound'))
        self.assertTemplateUsed(response, 'report_absent.html')
