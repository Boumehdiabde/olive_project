from datetime import date

from django.test import TestCase
from rest_framework.test import APIClient

from .models import Grove, Harvest, MaintenanceLog


class GrovePageTests(TestCase):
    def setUp(self):
        self.grove = Grove.objects.create(
            name="North Orchard",
            location="Alentejo",
            variety="Arbequina",
            tree_count=120,
            area_hectares=2.5,
            planting_year=2018,
        )

    def test_dashboard_shows_aggregated_values(self):
        Harvest.objects.create(
            grove=self.grove,
            harvest_date=date(2025, 11, 1),
            quantity=250.5,
        )

        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "North Orchard")
        self.assertEqual(response.context["total_trees"], 120)
        self.assertEqual(response.context["total_harvest"], 250.5)
        self.assertEqual(response.context["total_area"], 2.5)

    def test_grove_detail_includes_related_records(self):
        Harvest.objects.create(grove=self.grove, quantity=100)
        MaintenanceLog.objects.create(
            grove=self.grove,
            task_type="Pruning",
            description="Annual pruning",
        )

        response = self.client.get(f"/groves/{self.grove.pk}/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["harvests"].count(), 1)
        self.assertEqual(response.context["maintenance_logs"].count(), 1)

    def test_grove_detail_returns_404_for_missing_grove(self):
        self.assertEqual(self.client.get("/groves/9999/").status_code, 404)

    def test_invalid_status_filter_does_not_hide_all_groves(self):
        response = self.client.get("/groves/?status=not-a-status")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "North Orchard")


class OliveApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.grove = Grove.objects.create(
            name="South Orchard",
            location="Beja",
            variety="Picual",
            tree_count=80,
            area_hectares=1.75,
            planting_year=2020,
        )

    def test_stats_endpoint_returns_aggregates_and_empty_defaults(self):
        response = self.client.get("/api/stats/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["total_groves"], 1)
        self.assertEqual(response.data["total_trees"], 80)
        self.assertEqual(response.data["total_area"], 1.75)
        self.assertEqual(response.data["total_harvest"], 0)

    def test_harvest_api_accepts_grove_relationship(self):
        response = self.client.post("/api/harvests/", {
            "grove": self.grove.pk,
            "quantity": 125,
            "quality_grade": "A",
            "oil_yield": 22,
        }, format="json")

        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(response.data["grove"], self.grove.pk)
        self.assertEqual(Harvest.objects.count(), 1)

    def test_maintenance_api_accepts_grove_relationship(self):
        response = self.client.post("/api/maintenance/", {
            "grove": self.grove.pk,
            "task_type": "Pruning",
            "description": "Annual pruning",
            "cost": 40,
        }, format="json")

        self.assertEqual(response.status_code, 201, response.data)
        self.assertEqual(response.data["grove"], self.grove.pk)
        self.assertEqual(MaintenanceLog.objects.count(), 1)
