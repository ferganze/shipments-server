from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Shipment
from .serializers import ShipmentSerializer

class ShipmentsViewSet(GenericViewSet):
    serializer_class = ShipmentSerializer
    queryset = Shipment.objects.order_by('-created').all()
    # permission_classes = [DjangoObjectPermissions] # Django Object and Authentication permisions are disabled

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return self.get_paginated_response(self.paginate_queryset(serializer.data))

    def create(self, request):
        return self.save(request)

    def retrieve(self, request, pk=None):
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data)

    def update(self, request, pk=None):
        return self.save(request, pk)

    def destroy(self, request, pk=None):
        shipment = self.get_object()
        shipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def save(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if pk is None:
            shipment = serializer.create(serializer.data)
        else:
            shipment = serializer.update(self.get_object(), serializer.data)

        serializer = self.get_serializer(shipment)

        return Response(serializer.data, status=status.HTTP_200_OK)