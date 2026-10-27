from django.test import TestCase
from django.contrib.auth import get_user_model
from app.shipments.models import Shipment, TrackingEvent
from app.shipments.services import record_tracking_event
User = get_user_model()
# Create your tests here.

class ShipmentModelTestCase(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(
        username="testuser", 
         password="testpassword")
        
        self.shipment =Shipment.objects.create(
        customer=self.user,
        origin="chennai",
        destination="bangalore",
    )

    def test_tracking_event_updates_shipment_status(self):
        event=record_tracking_event(
            shipment=self.shipment,
            status="picked_up",
            location_description="chennai warehouse",
        )
        self.shipment.refresh_from_db()

        self.assertEqual(self.shipment.status, "picked_up")
        self.assertEqual(event.status, "picked_up")
        self.assertEqual(event.location_description, "chennai warehouse")


        def test_tracking_event_is_saved(self):
            record_tracking_event(
                shipment=self.shipment,
                status="in_transit",
                location_description="on the way to bangalore",

            )

            self.assertEqual(TrackingEvent.objects.filter(shipment=self.shipment).count(), 1)



class ShipmentTrackingTests(TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)