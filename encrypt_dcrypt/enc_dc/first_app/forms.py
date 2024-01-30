from django import forms
from .models import EncryptedFile

class EncryptedFileForm(forms.ModelForm):
    class Meta:
        model = EncryptedFile
        fields = ['file']