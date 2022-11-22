from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shipments_api.views import ShipmentsViewSet

router = DefaultRouter()
router.register(r'shipments', ShipmentsViewSet, basename='shipments')

urlpatterns = [
    path('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), # Authentication is disabled
]
