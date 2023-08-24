from rest_framework import serializers
from .models import Group

class GroupSerializer(serializers.ModelSerializer):
    subscribers_count = serializers.SerializerMethodField()
    avatar_name = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['name','avatar','subscribers_count', 'avatar_name']

    def get_subscribers_count(self, obj):
        return obj.subscribers.all().count()
    
    def get_avatar_name(self, obj):
        return obj.avatar.name