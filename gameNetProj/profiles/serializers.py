from rest_framework import serializers
from .models import UserImages

class UserImagesSerializer(serializers.ModelSerializer):
    image_name = serializers.SerializerMethodField()

    class Meta:
        model = UserImages
        fields = ['id','user_id','image', 'image_name']

    def get_image_name(self, obj):
        return obj.image.name