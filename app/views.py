import os

import magic
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, FileResponse, HttpResponseNotAllowed
from rest_framework import status
from django.http import JsonResponse
from app.forms import FileForm
from app.models import File
from storage_test_project import settings


def upload(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            hash_name = form.save()
            response = JsonResponse({'hash_name': str(hash_name)}, status=status.HTTP_200_OK)
            return response
        return HttpResponseBadRequest()
    return HttpResponseNotAllowed(permitted_methods='POST')


def download_or_delete(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        if 'hash_name' in request.POST:
            obj = File.objects.filter(file__contains=request.POST['hash_name'] + '.')
            if len(obj) > 0:
                obj = obj[0]
                path = settings.MEDIA_ROOT + "/" + str(obj.file)
                if request.path == '/download/':
                    file_type = magic.from_file(path, mime=True)
                    response = FileResponse(obj.file, content_type=file_type)
                elif request.path == '/delete/':
                    os.remove(path)
                    obj.delete()
                    response = JsonResponse(data={'info': "The file was deleted."}, status=status.HTTP_200_OK)
                return response
    return HttpResponseBadRequest()
