from django import forms
from manage_files.forms import UploadFileForm


class SplitForm(UploadFileForm, forms.Form):
    intervals = forms.CharField(required=False,
                                label='Страницы', widget=forms.TextInput(attrs={'placeholder': '1-3, 4'}))
    step = forms.IntegerField(
        required=False, label='Страниц в файле', min_value=1)
