import hashlib
import os
from typing import Tuple

from django.db import models

from storage_test_project import settings


def get_path(instance, filename: str):
    name = get_name(instance, filename)
    path = name[:2] + '/' + name
    if os.path.exists(os.path.join(settings.MEDIA_ROOT, path)):
        os.remove(os.path.join(settings.MEDIA_ROOT, path))
    return path


def get_name(instance, filename: str):
    name, file_type = parse_file_name(filename)
    name = str(hashlib.sha256(str(name).encode('utf-8')).hexdigest())
    return name + file_type


def parse_file_name(data: str) -> Tuple[str, str]:
    try:
        name = str(data).split('.')[0]
        file_type = '.' + str(data).split('.')[1]
    except:
        name, file_type = str(data), ''
    return name, file_type


class File(models.Model):
    file = models.FileField(upload_to=get_path, blank=False, unique=True)

    def __str__(self):
        return str(self.file)[3:].split('.')[0]


