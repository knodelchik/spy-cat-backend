from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from agency.views import SpyCatViewSet, MissionViewSet, TargetViewSet

# Створюємо роутер
router = DefaultRouter()
router.register(r'cats', SpyCatViewSet)
router.register(r'missions', MissionViewSet)
router.register(r'targets', TargetViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Підключаємо всі наші маршрути (cats, missions, targets)
    path('', include(router.urls)),
]