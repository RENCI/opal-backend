from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework.serializers import ModelSerializer
from .models import pfas_name_classification_info, pfas_in_tapwater_usgs, pfas_sample_data, pfas_sample_data2, ntar_sample_data, pfas_sites_distance_from_npl, superfund_national_priorities_list, opal_site_distance_to_closest_superfund_site, pfas_sample_data_npl
from drf_queryfields import QueryFieldsMixin

# Serializer, with GeoFeatureModelSerializer, for tables for the gauge_station_source_data model view.
# GeoFeatureModelSerializer enables spatial searches.

class pfas_name_classification_info_Serializer(QueryFieldsMixin, ModelSerializer):
    class Meta: 
        model = pfas_name_classification_info
        id_field = 'id'
        fields = ('abbreviation','chemical_name','casrn','dtxsid','nhanes','carbon_atoms','formula','pfaa','pfca','pfsa','precursor','ftbs','dipap','ftoh','acid_ftca','acid_fts','substances_pasf','sulfonamides_fasa','ethanols_fase','pfeca','pfesa','cl_pfesa','carboxylic_acid','sulfonic_acid')

class pfas_in_tapwater_usgs_Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = pfas_in_tapwater_usgs
        id_field = 'id'
        geo_field = 'geom'
        fields = ('id', 'study', 'station_na', 'site_type', 'sampleyear', 'detects', 'sum_pfas', 'pfprs', 'pfpes', 'pfpea', 'pfos', 
                  'pfoa', 'pfhxs', 'pfhxa', 'pfhps', 'pfhpa', 'pfds_num', 'pfda_num', 'pfbs', 'pfba', 'pf', 'genx_num', 'fosa', 
                  'f6_2fts', 'latitude', 'longitude')

class pfas_sample_data_Serializer(QueryFieldsMixin, ModelSerializer):
    class Meta:
        model = pfas_sample_data
        id_field = 'id'
        fields = ('id', 'sample_id', 'group_id', 'study', 'date', 'year', 'pi', 'units', 'medium', 'city', 'state', 'zipcode', 'site_id', 'site_type', 'latitude', 'longitude', 'sample_detects', 'sample_sum', 'pfna_concentration','pfna_mrl','pfna_dl','pfna_flags','pfds_concentration','pfds_mrl','pfds_dl','pfds_flags','pfhxa_concentration','pfhxa_mrl','pfhxa_dl','pfhxa_flags','pfoa_concentration','pfoa_mrl','pfoa_dl','pfoa_flags','pfos_concentration','pfos_mrl','pfos_dl','pfos_flags','pfba_concentration','pfba_mrl','pfba_dl','pfba_flags','pfdoa_concentration','pfdoa_mrl','pfdoa_dl','pfdoa_flags','pfpea_concentration','pfpea_mrl','pfpea_dl','pfpea_flags','pfhps_concentration','pfhps_mrl','pfhps_dl','pfhps_flags','pfunda_concentration','pfunda_mrl','pfunda_dl','pfunda_flags','pfbs_concentration','pfbs_mrl','pfbs_dl','pfbs_flags','pfpes_concentration','pfpes_mrl','pfpes_dl','pfpes_flags','pfns_concentration','pfns_mrl','pfns_dl','pfns_flags','pfhpa_concentration','pfhpa_mrl','pfhpa_dl','pfhpa_flags','pfhxs_concentration','pfhxs_mrl','pfhxs_dl','pfhxs_flags','pfda_concentration','pfda_mrl','pfda_dl','pfda_flags')

class pfas_sample_data2_Serializer(QueryFieldsMixin, ModelSerializer):
    class Meta:
        model = pfas_sample_data2
        id_field = 'id'
        fields = ('id', 'sample_id', 'study', 'date', 'year', 'pi', 'units', 'medium', 'site_id', 'site_type', 'latitude', 'longitude', 'sample_detects', 'sample_sum', 'pfmpa_concentration', 'pfmpa_mrl', 'pfmba_concentration', 'pfmba_mrl', 'pfta_concentration', 'pfta_mrl', 'netfosaa_concentration', 'netfosaa_mrl', 'x82fts_concentration', 'x82fts_mrl', 'hfpoda_concentration', 'hfpoda_mrl', 'x62fts_concentration', 'x62fts_mrl', 'nfdha_concentration', 'nfdha_mrl', 'pfuna_concentration', 'pfuna_mrl', 'pfeesa_concentration', 'pfeesa_mrl', 'nmefosaa_concentration', 'nmefosaa_mrl', 'x9clpf3ons_concentration', 'x9clpf3ons_mrl', 'x11clpf3ouds_concentration', 'x11clpf3ouds_mrl', 'adona_concentration', 'adona_mrl', 'x42fts_concentration', 'x42fts_mrl', 'pftrda_concentration', 'pftrda_mrl', 'genx_concentration', 'fosa_concentration', 'f6_2fts_concentration', 'pfprs_concentration')

class ntar_sample_data_Serializer(QueryFieldsMixin, ModelSerializer):
    class Meta:
        model = ntar_sample_data
        id_field = 'id'
        fields = ('id', 'sample_id', 'study', 'year', 'date', 'pi', 'medium', 'city', 'state', 'zipcode', 'site_id', 'site_type', 'latitude', 'longitude', 'sample_detects', 'sample_sum', 'pfas_short_name', 'pfas_long_name', 'flags', 'measurement')

class pfas_sites_distance_from_npl_Serializer(ModelSerializer):
    class Meta:
        model = pfas_sites_distance_from_npl
        id_field = 'pfas_sample_id'
        fields = ('pfas_sample_id','study','miles','pi','units','medium','pfas_longitude','pfas_latitude','ogc_fid','npl_site_name','npl_latitude','npl_longitude')

class opal_site_distance_to_closest_superfund_site_Serializer(QueryFieldsMixin, ModelSerializer):
    class Meta:
        model = opal_site_distance_to_closest_superfund_site
        id_field = 'opal_id'
        fields = ('opal_id','opal_site_sample_id', 'superfund_ogc_fid', 'miles_to_closest_superfund_site')

class superfund_national_priorities_list_Serializer(QueryFieldsMixin, ModelSerializer):
    class Meta:
        model = superfund_national_priorities_list
        id_field = 'ogc_fid'
        fields = ('ogc_fid','objectid','site_name','site_score','site_epa_i','sems_id','sits_id','region_id','state','city','county','status','longitude','latitude','proposed_d','listing_da','constructi','construc_1','noid_date','deletion_d','site_listi','site_progr','notice_of','proposed_f','deletion_f','final_fr_n','noid_fr_no','restoratio','site_has_h','creationda','creator','editdate','editor','objectid2','pfas')

class pfas_sample_data_npl_Serializer(QueryFieldsMixin, ModelSerializer):
    class Meta:
        model = pfas_sample_data_npl
        id_field = 'id'
        fields = ('id', 'sample_id', 'group_id', 'study', 'date', 'year', 'pi', 'units', 'medium', 'city', 'state', 'zipcode', 'site_id', 'site_type', 'latitude', 'longitude', 'superfund_ogc_fid', 'miles_to_closest_superfund_site', 'sample_detects', 'sample_sum', 'pfna_concentration','pfna_mrl','pfna_dl','pfna_flags','pfds_concentration','pfds_mrl','pfds_dl','pfds_flags','pfhxa_concentration','pfhxa_mrl','pfhxa_dl','pfhxa_flags','pfoa_concentration','pfoa_mrl','pfoa_dl','pfoa_flags','pfos_concentration','pfos_mrl','pfos_dl','pfos_flags','pfba_concentration','pfba_mrl','pfba_dl','pfba_flags','pfdoa_concentration','pfdoa_mrl','pfdoa_dl','pfdoa_flags','pfpea_concentration','pfpea_mrl','pfpea_dl','pfpea_flags','pfhps_concentration','pfhps_mrl','pfhps_dl','pfhps_flags','pfunda_concentration','pfunda_mrl','pfunda_dl','pfunda_flags','pfbs_concentration','pfbs_mrl','pfbs_dl','pfbs_flags','pfpes_concentration','pfpes_mrl','pfpes_dl','pfpes_flags','pfns_concentration','pfns_mrl','pfns_dl','pfns_flags','pfhpa_concentration','pfhpa_mrl','pfhpa_dl','pfhpa_flags','pfhxs_concentration','pfhxs_mrl','pfhxs_dl','pfhxs_flags','pfda_concentration','pfda_mrl','pfda_dl','pfda_flags')
