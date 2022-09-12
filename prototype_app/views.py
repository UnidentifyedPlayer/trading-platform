import mimetypes
import ntpath
import os

from django.http import FileResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, renderers, permissions
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.exceptions import APIException
from rest_framework.decorators import action, parser_classes
from prototype_app.serializers import UserSerializer, \
    GroupSerializer, ContractorListSerializer, CountryListSerializer

from django.db import models
from .query_generation import proccess_query
from .models import Contractor, Country, ContractorFullData
from .forms import UploadFileForm


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

class NoFile(APIException):
    status_code = 204
    default_detail = 'No content found.'
    default_code = 'no_content'


class ContractorFilter(filters.FilterSet):
    class Meta:
        model = Contractor
        fields = {
            'lbl': ['exact', 'contains', 'startswith', 'endswith', 'isnull'],
            'name_full': ['exact', 'contains', 'startswith', 'endswith', 'isnull'],
            'address': ['exact', 'contains', 'startswith', 'endswith', 'isnull'],
            'inn': ['exact', 'contains', 'startswith', 'endswith', 'isnull'],
            'kpp': ['exact', 'contains', 'startswith', 'endswith', 'isnull']
        }


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
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ContractorFilter

    def get_queryset(self):
        queryset = Contractor.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset

    @action(methods=['get'], detail=True, renderer_classes=(PassthroughRenderer,))
    def download_charter(self, *args, **kwargs):
        contractor_id = self.get_object().id
        instance = ContractorFullData.objects.get(id=contractor_id)
        if instance.fn_charter == None:
            raise NoFile()
        print(type(instance.fd_charter))

        # send file
        response = FileResponse(instance.fd_charter, content_type=instance.ft_charter)
        # response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.fn_charter

        return response

    @action(methods=['post'], detail=True)
    def upload_charter(self, request, *args, **kwargs):
        contractor_id = self.get_object().id
        instance = ContractorFullData.objects.get(id=contractor_id)
        print(instance.id)
        file = request.FILES.get('file')
        if file == None:
            raise NoFile()
        instance.fn_charter = file.name
        instance.ft_charter = file.content_type

        file_data = file.read()
        print(type(file_data))
        instance.fd_charter = file_data

        instance.save()
        # print(file)
        # if (instance.fd_charter == None):
        #     raise NoFile()
        # print(instance.fd_charter.path)

        return Response(status=200)




    @action(methods=['get'], detail=True, renderer_classes=(PassthroughRenderer,))
    def download_file(self, *args, **kwargs):
        contractor_id = self.get_object().id
        instance = ContractorFullData.objects.get(id=contractor_id)
        print(instance.fl_egryul)
        if instance.fl_egryul == None:
            return Response(status=204)
        if not os.path.exists(instance.fl_egryul):
            return Response(status=204)

        path = open(instance.fl_egryul, 'rb')
        mime_type, _ = mimetypes.guess_type(instance.fl_egryul)
        filename = path_leaf(instance.fl_egryul)


        # send file
        response = FileResponse(path, content_type=mime_type)
        # response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename
        print(mime_type)
        print(filename)
        return response


    def handle_uploaded_file(self, f):
        contractor_id = self.get_object().id
        instance = ContractorFullData.objects.get(id=contractor_id)
        prev_file = instance.fl_egryul
        if (prev_file is not None) and (os.path.isfile(prev_file)):
            prev_file = instance.fl_egryul
            os.remove(prev_file)

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = BASE_DIR + "\\files\\" + str(contractor_id)
        if not os.path.isdir(filepath):
            os.mkdir(filepath)
        filepath = filepath + "\\egryul\\"
        if not os.path.isdir(filepath):
            os.mkdir(filepath)
        filepath = filepath + f.name

        print(filepath)


        with open(filepath, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

        instance.fl_egryul = filepath
        instance.save()

    @action(methods=['post'], detail=True)
    def upload_file(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            #print(form)
            if form.is_valid():
                self.handle_uploaded_file(request.FILES['file'])
                return Response(status=200)
        else:
            form = UploadFileForm()
            return Response(status=501)
        return Response(status=400)


    @action(methods=['delete'], detail=True)
    def remove_file(self, *args, **kwargs):
        contractor_id = self.get_object().id
        instance = ContractorFullData.objects.get(id=contractor_id)
        print(instance.fl_egryul)
        if instance.fl_egryul == None:
            return Response(status=204)
        if not os.path.exists(instance.fl_egryul):
            return Response(status=204)

        os.remove(instance.fl_egryul)
        instance.fl_egryul = None
        instance.save()
        return Response(status=200)


    @action(methods=['post'], detail=False)
    def filter(self, request, *args, **kwargs):
        query = request.data["query"]
        #print(query)
        q_query = proccess_query(query)
        #print(q_query)
        if q_query is not None:
            queryset = Contractor.objects.filter(q_query)
        else:
            queryset = self.get_queryset()
        print(queryset.query)

        sort = request.data.get("sort")
        if sort is not None:
            field = sort.get("field")
            if sort.get("field") == "desc":
                field = "-"+field
            queryset = queryset.order_by(field)


        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        # query_cond = query['cond']
        # for subquery in query_cond:
        #     print(subquery['fitler'])
        # print(request)


        return Response(serializer.data)



class CountryListViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer
    permission_classes = [permissions.AllowAny]

# Create your views here.
