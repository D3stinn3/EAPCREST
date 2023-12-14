from rest_framework import serializers
from apievent.models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'date', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
        
