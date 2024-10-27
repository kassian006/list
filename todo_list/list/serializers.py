from rest_framework import serializers
from .models import *


class TaskSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created']
