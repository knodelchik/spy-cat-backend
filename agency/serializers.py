from rest_framework import serializers
from .models import SpyCat, Mission, Target
import requests

class SpyCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpyCat
        fields = '__all__'

    def validate_breed(self, value):
        # Валідація породи через TheCatAPI
        url = "https://api.thecatapi.com/v1/breeds"
        response = requests.get(url)
        if response.status_code == 200:
            breeds = [b['name'].lower() for b in response.json()]
            if value.lower() not in breeds:
                 # Для тесту можна закоментувати raise, якщо API недоступне
                raise serializers.ValidationError("Invalid breed according to TheCatAPI.")
        return value

class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = ['id', 'name', 'country', 'notes', 'is_completed']

    def validate(self, data):
        # Заборона змінювати нотатки, якщо ціль або місія завершена
        if self.instance: # Якщо ми оновлюємо існуючий запис
            mission_complete = self.instance.mission.is_completed
            target_complete = self.instance.is_completed
            
            if (mission_complete or target_complete) and 'notes' in data:
                if data['notes'] != self.instance.notes:
                    raise serializers.ValidationError("Cannot update notes because target or mission is completed.")
        return data

class MissionSerializer(serializers.ModelSerializer):
    targets = TargetSerializer(many=True) # Вкладені цілі

    class Meta:
        model = Mission
        fields = ['id', 'cat', 'is_completed', 'targets']

    def validate_targets(self, value):
        if not (1 <= len(value) <= 3):
            raise serializers.ValidationError("A mission must have between 1 and 3 targets.")
        return value

    def create(self, validated_data):
        targets_data = validated_data.pop('targets')
        mission = Mission.objects.create(**validated_data)
        for target_data in targets_data:
            Target.objects.create(mission=mission, **target_data)
        return mission