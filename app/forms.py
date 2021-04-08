from django import forms

from app.models import File


class FileForm(forms.ModelForm):
    file = forms.FileField(label='Файл')

    class Meta:
        model = File
        fields = ('file',)
