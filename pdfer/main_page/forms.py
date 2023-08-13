from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(label="File Name", max_length=50)
    file = forms.FileField(
        label="File upload")
