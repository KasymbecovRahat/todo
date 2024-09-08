from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import *
from .serialazers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filter import TaskFilter
from rest_framework.filters import SearchFilter

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerialazer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = TaskFilter
    search_fields = ['title']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
