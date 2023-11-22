from tempfile import TemporaryDirectory
from http import HTTPStatus
from django.test import TestCase, Client


class TestCompress(TestCase):
    '''TODO: finish test_file_field'''

    def setUp(self):
        self.client = Client()
        self.response = self.client.get('')

    def test_template_name(self):
        self.assertTemplateUsed(
            self.response, 'compress_pdf/compress_pdf.html')

    def test_status_code(self):
        self.assertEqual(self.response.status_code, HTTPStatus.OK)

    def test_title(self):
        self.assertEqual(self.response.context['title'], 'Сжатие документа')

    def test_file_field(self):
        with TemporaryDirectory(dir='media/') as tmp_dir:
            with open(tmp_dir + 'test.pdf', 'wb') as test_pdf:
                test_pdf.write(b"I'm a pdf file!")
            with open(tmp_dir + 'test.txt', 'w') as test_txt:
                test_txt.write("I'm not a pdf file!")
            self.assertFieldOutput(MultipleFileField,
                                   valid={'file_field': test_pdf},
                                   invalid={'file_field': test_txt})
