from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import SpyCat, Mission, Target
from .serializers import SpyCatSerializer, MissionSerializer, TargetSerializer

class SpyCatViewSet(viewsets.ModelViewSet):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer

class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def perform_destroy(self, instance):
        if instance.cat:
            raise Exception("Cannot delete mission assigned to a cat")
        instance.delete()

class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
    
    # Автоматична перевірка завершення місії при оновленні цілі
    def perform_update(self, serializer):
        target = serializer.save()
        mission = target.mission
        if all(t.is_completed for t in mission.targets.all()):
            mission.is_completed = True
            mission.save()