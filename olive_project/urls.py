from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views

router = DefaultRouter()
router.register(r'groves', views.GroveViewSet)
router.register(r'harvests', views.HarvestViewSet)
router.register(r'maintenance', views.MaintenanceLogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('groves/', views.groves_list, name='groves_list'),
    path('groves/<int:pk>/', views.grove_detail, name='grove_detail'),
    path('api/', include(router.urls)),
    path('api/stats/', views.dashboard_stats, name='dashboard_stats'),
]
