from django.shortcuts import render
from app.shipments.models import Shipment, TrackingEvent
from app.shipments.serializers import ShipmentSerializer, TrackingEventSerializer
from rest_framework.decorators import api_view  
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def shipment_list(request):
    shipments = Shipment.objects.all()
    serializer = ShipmentSerializer(shipments, many=True)
    return Response(serializer.data)