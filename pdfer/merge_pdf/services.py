from PyPDF2 import PdfWriter, PdfReader


def merge_pdf_service(filenames: list) -> None:
    '''Merges given files'''
    '''TODO: make it work with django. Min 2 files'''

    with open('Merged_files.pdf', 'wb') as fout:
        writer = PdfWriter()
        for filename in filenames:
            file = PdfReader(filename)
            writer.append(file)
        writer.write(fout)
