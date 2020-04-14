from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)
