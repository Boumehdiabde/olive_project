from django.db.models import Sum
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Grove, Harvest, MaintenanceLog
from .serializers import GroveSerializer, HarvestSerializer, MaintenanceLogSerializer


def _dashboard_totals():
    """Return aggregate values without loading every record into Python."""
    grove_totals = Grove.objects.aggregate(
        total_trees=Sum("tree_count"),
        total_area=Sum("area_hectares"),
    )
    harvest_totals = Harvest.objects.aggregate(total_harvest=Sum("quantity"))
    return {
        "total_groves": Grove.objects.count(),
        "total_trees": grove_totals["total_trees"] or 0,
        "total_area": grove_totals["total_area"] or 0,
        "total_harvest": harvest_totals["total_harvest"] or 0,
    }


class GroveViewSet(viewsets.ModelViewSet):
    queryset = Grove.objects.all()
    serializer_class = GroveSerializer


class HarvestViewSet(viewsets.ModelViewSet):
    queryset = Harvest.objects.select_related("grove").all()
    serializer_class = HarvestSerializer


class MaintenanceLogViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceLog.objects.select_related("grove").all()
    serializer_class = MaintenanceLogSerializer


@api_view(["GET"])
def dashboard_stats(request):
    """Return aggregate statistics for the dashboard."""
    return Response(_dashboard_totals())


def home(request):
    """Render the dashboard and its recent groves."""
    context = _dashboard_totals()
    context["groves"] = Grove.objects.all()[:5]
    return render(request, "core/home.html", context)


def groves_list(request):
    """Render groves, optionally filtered by a valid status."""
    groves = Grove.objects.all()
    status_filter = request.GET.get("status")
    valid_statuses = {value for value, _label in Grove.STATUS}
    if status_filter in valid_statuses:
        groves = groves.filter(status=status_filter)

    return render(request, "core/groves_list.html", {
        "groves": groves,
        "statuses": Grove.STATUS,
    })


def grove_detail(request, pk):
    """Render a grove and its related records."""
    grove = get_object_or_404(Grove, pk=pk)
    return render(request, "core/grove_detail.html", {
        "grove": grove,
        "harvests": grove.harvests.all(),
        "maintenance_logs": grove.maintenance_logs.all(),
    })
