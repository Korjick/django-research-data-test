from django.urls import path

from meta_form import views

app_name = 'meta_form'
urlpatterns = [
    path('', views.index, name='index'),
    path('download/<int:metadata_id>/', views.download_all_metadata, name='download_metadata')
]