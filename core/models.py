from django.db import models
from django.utils import timezone

class Grove(models.Model):
    VARIETIES = [
        ("Koroneiki", "Koroneiki"),
        ("Arbequina", "Arbequina"),
        ("Picual", "Picual"),
        ("Frantoio", "Frantoio"),
    ]

    STATUS = [
        ("Active", "Active"),
        ("Dormant", "Dormant"),
        ("New", "New Planting"),
    ]

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    variety = models.CharField(max_length=50, choices=VARIETIES)
    tree_count = models.IntegerField()
    area_hectares = models.FloatField()
    planting_year = models.IntegerField()
    irrigation_type = models.CharField(max_length=50, default="Drip")
    soil_type = models.CharField(max_length=50, default="Loam")
    status = models.CharField(max_length=20, choices=STATUS, default="Active")
    notes = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Harvest(models.Model):
    GRADE_CHOICES = [
        ("A", "Grade A - Premium"),
        ("B", "Grade B - Standard"),
        ("C", "Grade C - Lower"),
    ]

    grove = models.ForeignKey(Grove, on_delete=models.CASCADE, related_name='harvests')
    harvest_date = models.DateField(default=timezone.now)
    quantity = models.FloatField(help_text="Quantity in kg")
    quality_grade = models.CharField(max_length=1, choices=GRADE_CHOICES, default="B")
    oil_yield = models.FloatField(help_text="Oil yield percentage", default=20.0)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-harvest_date']

    def __str__(self):
        return f"{self.grove.name} - {self.harvest_date}"


class MaintenanceLog(models.Model):
    TASK_TYPES = [
        ("Pruning", "Pruning"),
        ("Irrigation", "Irrigation"),
        ("Fertilization", "Fertilization"),
        ("Pest Control", "Pest Control"),
        ("Disease Treatment", "Disease Treatment"),
    ]

    grove = models.ForeignKey(Grove, on_delete=models.CASCADE, related_name='maintenance_logs')
    task_type = models.CharField(max_length=50, choices=TASK_TYPES)
    date = models.DateField(default=timezone.now)
    description = models.TextField()
    cost = models.FloatField(default=0.0)
    completed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.grove.name} - {self.task_type}"
