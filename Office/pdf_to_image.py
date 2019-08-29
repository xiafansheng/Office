# from pdf2image import convert_from_path
# pages = convert_from_path('中美贸易战的回顾与展望_余永定.pdf', 500)
# for page in pages:
#     page.save('out.jpg', 'JPEG')

# -*- coding: utf-8 -*-
# import io
# from wand.image import Image
# from wand.color import Color
# from PyPDF2 import PdfFileReader, PdfFileWriter
# import subprocess
# memo = {}

# def getPdfReader(filename):
#     reader = memo.get(filename, None)
#     if reader is None:
#         reader = PdfFileReader(filename, strict=False)
#     memo[filename] = reader
#     return reader
#
# def _run_convert(filename, page, res=120):
#     idx = page + 1
#     pdfile = getPdfReader(filename)
#     pageObj = pdfile.getPage(page)
#     dst_pdf = PdfFileWriter()
#     dst_pdf.addPage(pageObj)
#     pdf_bytes = io.BytesIO()
#     dst_pdf.write(pdf_bytes)
#     pdf_bytes.seek(0)
#     img = Image(file=pdf_bytes, resolution=res)
#     img.format = 'png'
#     img.compression_quality = 90
#     img.background_color = Color("white")
#     img_path = '%s%d.png' % (filename[:filename.rindex('.')], idx)
#     img.save(filename=img_path)
#     img.destroy()
#
#
# PDFTOPPMPATH = r"C:\Users\Administrator\Downloads\poppler-0.68.0\bin\pdftoppm.exe"
# PDFFILE = "'中美贸易战的回顾与展望_余永定.pdf'"
# subprocess.Popen('"%s" -png %s out' % (PDFTOPPMPATH, PDFFILE))


from pdf2image import convert_from_path, convert_from_bytes
import tempfile

def convert_pdftoimage(pdffile):  #,outpdffolder
    with tempfile.TemporaryDirectory() as path:
        image_from_path = convert_from_path(pdffile,dpi=200, output_folder=r'C:\Users\Administrator\Desktop\hands on ml for at', fmt='jpg')
    print('%s convert okay'%pdffile)
convert_pdftoimage(r'C:\Users\Administrator\Desktop\量化投资资料\量化教材\Hands－On_Machine_Learning_for_Algorithmic_Trading.pdf')