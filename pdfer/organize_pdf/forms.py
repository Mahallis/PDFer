from django import forms
from manage_files.forms import UploadFileForm


class OrganizeForm(UploadFileForm, forms.Form):
    pass

