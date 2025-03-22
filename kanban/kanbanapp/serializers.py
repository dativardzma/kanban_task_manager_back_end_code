from rest_framework import serializers
from .models import Table, SubTask, Blog

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"

class SubTaskSerializer(serializers.ModelSerializer):
    class Meta: 
        model = SubTask
        fields = ['title', 'description', 'status']

    def create(self, validated_data):
        validated_data['status'] = validated_data.get('status', 'not ready')
        return super().create(validated_data)

class BlogSerializer(serializers.ModelSerializer):
    subtasks = serializers.PrimaryKeyRelatedField(queryset=SubTask.objects.all(), many=True)
    class Meta:
        model = Blog
        fields = "__all__"

    def validate(self, attrs):
        table = attrs['table']  
        column = attrs['status']

        if column not in table.columns:
            raise serializers.ValidationError(f"Invalid column: {column}. Allowed: {table.columns}")

        return attrs

