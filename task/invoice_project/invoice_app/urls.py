from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router for Django Rest Framework viewsets
router = DefaultRouter()
router.register(r'invoices', views.InvoiceViewSet)
router.register(r'invoice-details', views.InvoiceDetailViewSet)

urlpatterns = [
    path('', views.invoices_list, name='invoices-list'),
    path('invoices/<int:invoice_id>/', views.invoice_detail, name='invoice-detail'),
    path('create-edit-invoice/', views.create_edit_invoice, name='create-edit-invoice'),
    path('api/', include(router.urls)),
]
