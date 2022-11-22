from .models import Shipment
from rest_framework.serializers import ModelSerializer, ChoiceField


class ShipmentSerializer(ModelSerializer):
    status = ChoiceField(choices=Shipment.STATUS_CHOICES, source='get_status_display')

    class Meta:
        model = Shipment
        fields = ['id', 'tracking_id', 'recipient', 'address', 'status', 'created', 'updated']
