from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Grove, Harvest

@api_view(['GET'])
def dashboard_stats(request):
    total_groves = Grove.objects.count()
    total_trees = sum(g.tree_count for g in Grove.objects.all())
    total_harvest = sum(h.quantity for h in Harvest.objects.all())

    return Response({
        "total_groves": total_groves,
        "total_trees": total_trees,
        "total_harvest": total_harvest
    })