
from django.urls import path

from app.shipments.views import shipment_list

urlpatterns = [
    path('shipments/', shipment_list, name='shipment-list'),
]
