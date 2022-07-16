from django.contrib.auth.models import User, Group
from prototype_app.models import Contractor, Country
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ContractorListSerializer(serializers.HyperlinkedModelSerializer):
    #country = serializers.ReadOnlyField(source='country.name')

    class Meta:
        model = Contractor
        fields = [
            'id', 'lbl', 'name_full', 'address', 'inn', 'kpp', 'list_work',
            'oe_start_date', 'scntr_num', 'credit_limit', 'country'
                  ]


class CountryListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = [
            'id', 'name', 'description'
                  ]