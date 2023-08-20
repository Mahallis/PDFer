from PyPDF2 import PdfReader, PdfWriter


def merge_pdf(filenames: list) -> None:
    '''Merges given files'''
    '''TODO: figure out how to merge several files. Maybe it is possible by handling files as list of pages'''
    with open('Merged_files.pdf', 'wb') as fout:
        writer = PdfWriter()
        for filename in filenames:
            file = PdfReader(filename)
            writer.append(file)
        writer.write(fout)
