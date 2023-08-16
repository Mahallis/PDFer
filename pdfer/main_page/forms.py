from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField(label="Поле для загрузки файла")
    is_grayscale = forms.BooleanField(
        label='Черно-белый документ', required=False)
    dpi = forms.IntegerField(label='Точек на дюйм',
                             min_value=100, max_value=300, step_size=50)
    quality = forms.IntegerField(
        label='Качество', min_value=30, max_value=100, step_size=10)
    resolution = forms.FloatField(
        label='Разрешение', min_value=10.0, max_value=100.0, step_size=10.0)
