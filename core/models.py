from django.db import models

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

    def __str__(self):
        return self.name