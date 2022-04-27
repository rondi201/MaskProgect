from django.urls import path
from . import views

urlpatterns = [
    path('', views.startpage, name="startpage"),
    path('upload', views.file_upload, name='upload-file'),
    path('result', views.resultpage, name="resultpage"),
]