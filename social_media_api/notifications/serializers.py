from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source='actor.username')
    recipient = serializers.ReadOnlyField(source='recipient.username')
    target = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = '__all__'

    def get_target(self, obj):
        if obj.target:
            return str(obj.target)
        return None