from django.contrib import admin
from django.urls import path, include
from app.views import upload, download_or_delete

urlpatterns = [
    path('upload/', upload),
    path('download/', download_or_delete),
    path('delete/', download_or_delete),
    ]