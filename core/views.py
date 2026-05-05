from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Grove, Harvest, MaintenanceLog
from .serializers import GroveSerializer, HarvestSerializer, MaintenanceLogSerializer


class GroveViewSet(viewsets.ModelViewSet):
    queryset = Grove.objects.all()
    serializer_class = GroveSerializer


class HarvestViewSet(viewsets.ModelViewSet):
    queryset = Harvest.objects.all()
    serializer_class = HarvestSerializer


class MaintenanceLogViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceLog.objects.all()
    serializer_class = MaintenanceLogSerializer


@api_view(['GET'])
def dashboard_stats(request):
    """Get dashboard statistics"""
    total_groves = Grove.objects.count()
    total_trees = sum(g.tree_count for g in Grove.objects.all())
    total_harvest = sum(h.quantity for h in Harvest.objects.all())
    total_area = sum(g.area_hectares for g in Grove.objects.all())

    return Response({
        "total_groves": total_groves,
        "total_trees": total_trees,
        "total_harvest": total_harvest,
        "total_area": total_area
    })


def home(request):
    """Home dashboard view"""
    groves = Grove.objects.all()[:5]
    total_groves = Grove.objects.count()
    total_trees = sum(g.tree_count for g in Grove.objects.all())
    total_harvest = sum(h.quantity for h in Harvest.objects.all())
    
    context = {
        'groves': groves,
        'total_groves': total_groves,
        'total_trees': total_trees,
        'total_harvest': total_harvest,
    }
    return render(request, 'core/home.html', context)


def groves_list(request):
    """List all groves"""
    groves = Grove.objects.all()
    status_filter = request.GET.get('status')
    
    if status_filter:
        groves = groves.filter(status=status_filter)
    
    context = {
        'groves': groves,
        'statuses': Grove.STATUS,
    }
    return render(request, 'core/groves_list.html', context)


def grove_detail(request, pk):
    """Grove detail view"""
    grove = get_object_or_404(Grove, pk=pk)
    harvests = grove.harvests.all()
    maintenance_logs = grove.maintenance_logs.all()
    
    context = {
        'grove': grove,
        'harvests': harvests,
        'maintenance_logs': maintenance_logs,
    }
    return render(request, 'core/grove_detail.html', context)
