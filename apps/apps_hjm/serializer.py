from rest_framework import serializers
from .models import Board, Resume


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'title', 'description', 'created_at', 'updated_at')


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('id', 'name', 'age', 'career', 'introduce', 'created_at', 'updated_at')
