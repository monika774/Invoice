from django.shortcuts import render, get_object_or_404, redirect
from .models import Invoice, InvoiceDetail
from .forms import InvoiceForm

def invoices_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoice_app/invoices_list.html', {'invoices': invoices})

def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    return render(request, 'invoice_app/invoice_detail.html', {'invoice': invoice})

def create_edit_invoice(request, invoice_id=None):
    if invoice_id:
        invoice = get_object_or_404(Invoice, id=invoice_id)
    else:
        invoice = Invoice()

    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('invoices-list')
    else:
        form = InvoiceForm(instance=invoice)

    return render(request, 'invoice_app/invoice_form.html', {'form': form})

from rest_framework import viewsets
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer

# ... Your existing code ...

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceDetailViewSet(viewsets.ModelViewSet):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer
