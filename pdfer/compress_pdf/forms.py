from django import forms
from manage_files.forms import UploadFileForm


class CompressForm(UploadFileForm, forms.Form):
    is_grayscale = forms.BooleanField(label='Черно-белый документ',
                                      required=False)
    dpi = forms.IntegerField(label='Точек на дюйм',
                             min_value=100, max_value=150, step_size=50)
    quality = forms.IntegerField(label='Качество',
                                 min_value=10,
                                 max_value=70,
                                 step_size=10)
