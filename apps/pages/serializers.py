from rest_framework import serializers
from .models import WebPage


class PagesSerializer(serializers.Serializer):
    url = serializers.URLField()

    def create(self, validated_data):
        return WebPage.objects.create(**validated_data)
