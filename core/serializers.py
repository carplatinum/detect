from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    original_image = serializers.ImageField()
    translated_image = serializers.ImageField(read_only=True)

    class Meta:
        model = Image
        fields = ['id', 'original_image', 'translated_image', 'created_at',
                  'text_original', 'text_translated', 'is_translated']
        read_only_fields = ['translated_image', 'created_at', 'text_original', 'text_translated', 'is_translated']
