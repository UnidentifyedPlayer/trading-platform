from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.http import FileResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, renderers, permissions
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.exceptions import APIException
from rest_framework.decorators import action, parser_classes
from prototype_app.serializers import UserSerializer,\
    GroupSerializer, ContractorListSerializer, CountryListSerializer

from django.db import models
from .models import Contractor, Country

class NoFile(APIException):
    status_code = 204
    default_detail = 'No content found.'
    default_code = 'no_content'



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


class PassthroughRenderer(renderers.BaseRenderer):
    """
        Return data as-is. View should supply a Response.
    """
    media_type = ''
    format = ''
    def render(self, data, accepted_media_type=None, renderer_context=None):
        return data


class ContractorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contractors to be viewed or edited.
    """
    serializer_class = ContractorListSerializer
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]
    parser_classes

    def get_queryset(self):
        queryset = Contractor.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset

    @action(methods=['get'], detail=True, renderer_classes=(PassthroughRenderer,))
    def download_charter(self, *args, **kwargs):
        instance = self.get_object()
        if instance.fn_charter==None:
            raise NoFile()
        print(type(instance.fd_charter))

        # send file
        response = FileResponse(instance.fd_charter, content_type=instance.ft_charter)
        #response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.fn_charter

        return response


    @action(methods=['post'], detail=True)
    def upload_charter(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance.id)
        file = request.FILES.get('file')
        if file==None:
            raise NoFile()
        instance.fn_charter = file.name
        instance.ft_charter = file.content_type

        file_data = file.read()
        print(type(file_data))
        instance.fd_charter = file_data

        instance.save()
        #print(file)
        # if (instance.fd_charter == None):
        #     raise NoFile()
        # print(instance.fd_charter.path)
        # get an open file handle (I'm just using a file attached to the model for this example):
        # file_handle = instance.fd_charter.open()

        # # send file
        # response = FileResponse(instance.fd_charter, content_type=instance.ft_charter)
        # # response['Content-Length'] = instance.file.size
        # response['Content-Disposition'] = 'attachment; filename="%s"' % instance.fn_charter

        return Response(status=200)
    # def perform_create(self, serializer):
    #     serializer.save(object_id=self.request.object_id, country=self.request.country_id)


class CountryListViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer
    permission_classes = [permissions.AllowAny]

# Create your views here.
