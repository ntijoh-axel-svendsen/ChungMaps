from rest_framework import serializers
from django.contrib.auth.models import User
from MapExplorer.models import MinecraftBlock


class MinecraftBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinecraftBlock
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    scanned_blocks = serializers.PrimaryKeyRelatedField(many=True, queryset=MinecraftBlock.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'scanned_blocks']
