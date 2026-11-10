from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="grove",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="grove",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name="Harvest",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("harvest_date", models.DateField(default=django.utils.timezone.now)),
                ("quantity", models.FloatField(help_text="Quantity in kg")),
                ("quality_grade", models.CharField(choices=[("A", "Grade A - Premium"), ("B", "Grade B - Standard"), ("C", "Grade C - Lower")], default="B", max_length=1)),
                ("oil_yield", models.FloatField(default=20.0, help_text="Oil yield percentage")),
                ("notes", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("grove", models.ForeignKey(on_delete=models.deletion.CASCADE, related_name="harvests", to="core.grove")),
            ],
            options={"ordering": ["-harvest_date"]},
        ),
        migrations.CreateModel(
            name="MaintenanceLog",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("task_type", models.CharField(choices=[("Pruning", "Pruning"), ("Irrigation", "Irrigation"), ("Fertilization", "Fertilization"), ("Pest Control", "Pest Control"), ("Disease Treatment", "Disease Treatment")], max_length=50)),
                ("date", models.DateField(default=django.utils.timezone.now)),
                ("description", models.TextField()),
                ("cost", models.FloatField(default=0.0)),
                ("completed", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("grove", models.ForeignKey(on_delete=models.deletion.CASCADE, related_name="maintenance_logs", to="core.grove")),
            ],
            options={"ordering": ["-date"]},
        ),
    ]
