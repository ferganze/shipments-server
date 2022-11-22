from django.db import models

class Shipment(models.Model):
    STATUS_NEW = 0
    STATUS_PROCESSING = 1
    STATUS_DELIVERED = 2
    STATUS_CLOSED = 3
    STATUS_CHOICES = [
        (STATUS_NEW, 'New'),
        (STATUS_PROCESSING, 'Processing'),
        (STATUS_DELIVERED, 'Delivered'),
        (STATUS_CLOSED, 'Closed'),
    ]

    tracking_id = models.CharField(max_length = 50)
    recipient = models.CharField(max_length = 100)
    address = models.CharField(max_length = 500)
    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_NEW)
    created = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now = True)
