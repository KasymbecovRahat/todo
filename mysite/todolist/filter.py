from django_filters import FilterSet
from .models import *

class TaskFilter(FilterSet):
    model = Task
    fields = {
            'created' :['gt , lt']
    }