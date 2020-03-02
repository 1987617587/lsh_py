from django.shortcuts import render

# Create your views here.
from .models import *
from rest_framework import viewsets
from .serializers import WorkersSerializers, DepartmentSerializers


# Create your views here.
class WorkersViewSet(viewsets.ModelViewSet):
    queryset = Workers.objects.all()
    serializer_class = WorkersSerializers


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers
