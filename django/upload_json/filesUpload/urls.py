from django.urls import path
from rest_framework import routers

from .views import FileUpload, ViewUploadedData

upload = FileUpload.as_view({
    'post': 'post',
})

view_file_data = ViewUploadedData.as_view({
    'get': 'get',
})

urlpatterns = [
    path('upload', upload, name="file_upload"),
    path('uploaded_data', view_file_data, name="uploaded_data")
]