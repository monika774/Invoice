

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice

class InvoiceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {'date': '2023-09-24', 'customer_name': 'Test Customer'}
        self.response = self.client.post('/api/invoices/', self.invoice_data, format='json')

    def test_create_invoice(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_invoice(self):
        invoice = Invoice.objects.get()
        response = self.client.get(f'/api/invoices/{invoice.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
