from rest_framework import serializers
from .models import Search


class LinksSerializer(serializers.Serializer):
    link = serializers.CharField()
    region = serializers.CharField()

    def create(self, validated_data):
        return Search.objects.create(**validated_data)