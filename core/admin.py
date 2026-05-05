from django.contrib import admin
from .models import Grove, Harvest, MaintenanceLog


class HarvestInline(admin.TabularInline):
    model = Harvest
    extra = 1


class MaintenanceLogInline(admin.TabularInline):
    model = MaintenanceLog
    extra = 1


@admin.register(Grove)
class GroveAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'variety', 'status', 'tree_count', 'created_at']
    list_filter = ['status', 'variety', 'created_at']
    search_fields = ['name', 'location']
    inlines = [HarvestInline, MaintenanceLogInline]
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'location', 'image_url')
        }),
        ('Grove Details', {
            'fields': ('variety', 'tree_count', 'area_hectares', 'planting_year')
        }),
        ('Management', {
            'fields': ('irrigation_type', 'soil_type', 'status')
        }),
        ('Notes', {
            'fields': ('notes',)
        }),
    )


@admin.register(Harvest)
class HarvestAdmin(admin.ModelAdmin):
    list_display = ['grove', 'harvest_date', 'quantity', 'quality_grade', 'oil_yield']
    list_filter = ['quality_grade', 'harvest_date']
    search_fields = ['grove__name']


@admin.register(MaintenanceLog)
class MaintenanceLogAdmin(admin.ModelAdmin):
    list_display = ['grove', 'task_type', 'date', 'cost', 'completed']
    list_filter = ['task_type', 'completed', 'date']
    search_fields = ['grove__name']
