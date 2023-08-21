from rest_framework import serializers
from .models import Group

class GroupSerializer(serializers.ModelSerializer):
    subscribers_count = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['name','avatar','subscribers_count']

    def get_subscribers_count(self, obj):
        return obj.subscribers.all().count()