from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.file_upload, name='uploadpage'),
    path('', views.resultpage, name="resultpage"),
]