from django import forms
from django.core.validators import FileExtensionValidator


class MultipleFileInput(forms.ClearableFileInput):
    '''Allows to select multiple files in form'''

    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    '''Adds the ability to handle multiple uploaded file'''

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            # Validates every uploaded file
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class CompressForm(forms.Form):
    file_field = MultipleFileField(label="Поле для загрузки файла",
                                   validators=[FileExtensionValidator(['pdf'], 'Выберите файл с расширением .pdf')])
    is_grayscale = forms.BooleanField(label='Сделать документ черно-белым',
                                      required=False)
    dpi = forms.IntegerField(label='Точек на дюйм',
                             min_value=100, max_value=150, step_size=50, initial=100)
    quality = forms.IntegerField(label='Качество',
                                 min_value=10,
                                 max_value=70,
                                 step_size=10,
                                 initial=60)
