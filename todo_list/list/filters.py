from django_filters import FilterSet
from .models import Task


class TaskFilter(FilterSet):
    class Meta:
        model = Task
        fields = {
            'created': ['gt', 'lt']
        }