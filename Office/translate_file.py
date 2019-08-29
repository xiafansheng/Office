import re
from Office.pdf_read import read_pdf
from googletrans import Translator

translator = Translator()

def translatefile(block,outputfile):
    translated = translator.translate(block, dest='zh-cn').text
    with open(outputfile ,'a+', encoding='utf-8',) as f:
        content = translated+ '\n'+ '\n' +'\n'
        f.write(content)
def writerworrd():
    pass

def wordtpdf():
    pass
path = ''
pdfcontent = read_pdf(path)
for p in pdfcontent:
    translatefile(p)