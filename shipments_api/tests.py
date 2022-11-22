from rest_framework.test import APITestCase
from rest_framework import status
from shipments_api.models import Shipment

class ShipmentsTestCase(APITestCase):
    url = '/api/shipments/'
    shipment = {
        'tracking_id': 'TRACKTEST09880923',
        'recipient': 'Jhon Leiser',
        'address': '9251 Taylor Lane, Pueblo, CO 81001',
        'status': Shipment.STATUS_NEW,
    }

    def setUp(self):
        self.created = self.client.post(self.url, self.shipment, format='json')

    def test_list(self):
        '''
        Test getting list of Shipments
        '''
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), Shipment.objects.count())
        self.assertTrue(response.data.get('results'))

    def test_create(self):
        '''
        Test creating a new Shipment
        '''
        response = self.client.post(self.url, self.shipment, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('tracking_id'), self.shipment.get('tracking_id'))

    def test_retrieve(self):
        '''
        Test getting the Shipment
        '''
        response = self.client.get(f"{self.url}{self.created.data['id']}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('tracking_id'), self.shipment.get('tracking_id'))

    def test_update(self):
        '''
        Test updating the Shipment
        '''
        self.created.data['status'] = Shipment.STATUS_DELIVERED
        response = self.client.put(f"{self.url}{self.created.data['id']}/", self.created.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('status'), dict(Shipment.STATUS_CHOICES)[Shipment.STATUS_DELIVERED])

    def test_delete(self):
        '''
        Test deleting the Shipment
        '''
        response = self.client.delete(f"{self.url}{self.created.data['id']}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
