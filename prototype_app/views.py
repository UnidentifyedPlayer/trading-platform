from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from prototype_app.serializers import UserSerializer,\
    GroupSerializer, ContractorListSerializer, CountryListSerializer

from django.db import models
from .models import Contractor, Country


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ContractorListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Contractor.objects.filter(country=289713190000)
    serializer_class = ContractorListSerializer
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]


    # def perform_create(self, serializer):
    #     serializer.save(object_id=self.request.object_id, country=self.request.country_id)


class CountryListViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer
    permission_classes = [permissions.AllowAny]

# Create your views here.
