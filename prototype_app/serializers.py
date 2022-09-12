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


def get_country_choice():
    countries = Country.objects.all()
    choice_list = [(country.id, country.name) for country in countries]
    return choice_list


class CountryListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = [
            'id', 'name'
                  ]


class ContractorListSerializer(serializers.HyperlinkedModelSerializer):
    #telephone = serializers.CharField(write_only=True, required=False)
    #id = serializers.ReadOnlyField()
    #country = CountryListSerializer(many=False, read_only=True)
    country_info = CountryListSerializer(source='country', read_only=True)

    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.prefetch_related('country')
        return queryset

    class Meta:
        model = Contractor
        fields = [
            'id', 'lbl', 'name_full', 'address', 'inn', 'kpp', 'list_work',
            'oe_start_date', 'scntr_num', 'credit_limit',
            'country', 'country_info', 'telephone'
                  ]
        extra_kwargs = {'country': {'write_only': True},
                        'telephone': {'write_only': True, 'required': False},
                        'id': {'read_only': True}}

class ContractorInstanceSerializer(serializers.HyperlinkedModelSerializer):
    #telephone = serializers.CharField(write_only=True, required=False)
    #id = serializers.ReadOnlyField()
    #country = CountryListSerializer(many=False, read_only=True)
    country_info = CountryListSerializer(source='country', read_only=True)

    @staticmethod
    def setup_eager_loading(queryset):
        """ Perform necessary eager loading of data. """
        queryset = queryset.prefetch_related('country')
        return queryset

    class Meta:
        model = Contractor
        fields = [
            'id', 'lbl', 'name_full', 'address', 'inn', 'kpp', 'list_work',
            'oe_start_date', 'scntr_num', 'credit_limit',
            'country', 'country_info', 'telephone'
                  ]
        extra_kwargs = {'country': {'write_only': True},
                        'telephone': {'write_only': True, 'required': False},
                        'id': {'read_only': True}}



