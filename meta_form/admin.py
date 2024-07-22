from django.contrib import admin

from meta_form.models import ResearchMetadata, DataFormat, DegreeOfAggregation


@admin.register(DataFormat)
class DataFormatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(DegreeOfAggregation)
class DegreeOfAggregationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')


@admin.register(ResearchMetadata)
class ResearchMetadataAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_provider', 'data_format', 'degree_of_aggregation')
    list_display_links = ('id', 'data_provider')
    # list_editable = ('data_format', 'degree_of_aggregation')
    ordering = ['-created_at', 'data_provider']
    search_fields = ['data_provider']
    list_filter = ['data_format__name', 'degree_of_aggregation__name']
