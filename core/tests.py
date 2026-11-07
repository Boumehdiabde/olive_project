from rest_framework.test import APITestCase
from .models import Grove, Harvest, MaintenanceLog


class RelatedRecordAPITests(APITestCase):
    def setUp(self):
        self.grove = Grove.objects.create(
            name='Test Grove',
            location='Test Location',
            variety='Koroneiki',
            tree_count=100,
            area_hectares=2.5,
            planting_year=2020,
        )

    def test_create_harvest_with_grove(self):
        response = self.client.post('/api/harvests/', {
            'grove': self.grove.pk,
            'quantity': 125.5,
        }, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['grove'], self.grove.pk)
        self.assertTrue(Harvest.objects.filter(grove=self.grove, quantity=125.5).exists())

    def test_create_maintenance_log_with_grove(self):
        response = self.client.post('/api/maintenance/', {
            'grove': self.grove.pk,
            'task_type': 'Pruning',
            'description': 'Annual pruning',
        }, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['grove'], self.grove.pk)
        self.assertTrue(MaintenanceLog.objects.filter(grove=self.grove, task_type='Pruning').exists())
