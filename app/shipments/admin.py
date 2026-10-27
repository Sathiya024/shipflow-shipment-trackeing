from django.contrib import admin
from .models import Shipment,TrackingEvent

# Register your models here.
admin.site.register(Shipment)
admin.site.register(TrackingEvent)