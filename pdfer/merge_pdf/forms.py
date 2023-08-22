from django.forms import forms
from manage_files.forms import UploadFileForm


class MergeForm(UploadFileForm, forms.Form):
    pass
