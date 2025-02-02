from django.shortcuts import render

from api.models import Company
from api.serializers import CompanySerializer
from rest_framework import viewsets

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer