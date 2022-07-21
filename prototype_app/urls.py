from django.urls import include, path
from prototype_app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'contractor', views.ContractorViewSet, basename="contractor")
router.register(r'country', views.CountryListViewSet, basename="country")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
app_name = 'prototype_app'
urlpatterns = [
    path('', include(router.urls)),
]
