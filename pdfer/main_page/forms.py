from django import forms


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class UploadFileForm(forms.Form):
    file_field = MultipleFileField(label="Поле для загрузки файла")
    is_grayscale = forms.BooleanField(
        label='Черно-белый документ', required=False)
    dpi = forms.IntegerField(label='Точек на дюйм',
                             min_value=100, max_value=300, step_size=50)
    quality = forms.IntegerField(
        label='Качество', min_value=30, max_value=100, step_size=10)
    resolution = forms.FloatField(
        label='Разрешение', min_value=10.0, max_value=100.0, step_size=10.0)
