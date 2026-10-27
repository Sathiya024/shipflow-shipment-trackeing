from django.db import transaction
from django.utils import timezone

from app.shipments.models import Shipment,TrackingEvent

@transaction.atomic
def record_tracking_event(
    shipment,
    status,
    location_description="",
    latitude=None,
    longitude=None,
    occurred_at=None,
):
    shipment = Shipment.objects.select_for_update().get(id=shipment.id)
    even =TrackingEvent.objects.create(
        shipment=shipment,
        status=status,
        location_description=location_description,
        latitude=latitude,
        longitude=longitude,
        occurred_at=occurred_at or timezone.now(),
    )

    shipment.status = status
    shipment.save(update_fields=["status", "updated_at"])
    return even