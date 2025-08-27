"""Map URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path as url
from django.urls import path, include
from rest_framework import routers
from . import views

# Set URL for gauge geometry Django views
router = routers.DefaultRouter()

router.register(r'pfas_name_classification_info', views.podm_pfas_name_classification_info_View, 'pfas_name_classification_info')
router.register(r'pfas_in_tapwater_usgs', views.podm_pfas_in_tapwater_usgs_View, 'pfas_in_tapwater_usgs')
router.register(r'pfas_sample_data', views.podm_pfas_sample_data_View, 'pfas_sample_data')
router.register(r'pfas_sample_data2', views.podm_pfas_sample_data2_View, 'pfas_sample_data2')
router.register(r'ntar_sample_data', views.podm_ntar_sample_data_View, 'ntar_sample_data')
router.register(r'distance_from_npl', views.pfas_sites_distance_from_npl_View, basename='distance_from_npl')
router.register(r'superfund_npl', views.superfund_national_priorities_list_View, basename='superfund_npl')
router.register(r'opal_distance_to_npl', views.opal_site_distance_to_closest_superfund_site_View, basename='opal_distance_to_npl')
router.register(r'pfas_sample_data_npl', views.opal_pfas_sample_data_npl_View, 'pfas_sample_data_npl')

urlpatterns = [
    path("api/", include(router.urls)),
]

