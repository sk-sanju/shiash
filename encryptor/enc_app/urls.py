from django.urls import path
from .views import home, upload_file, view_file

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload_file, name='upload_file'),
    path('view/<int:file_id>/', view_file, name='view_file'),
]
