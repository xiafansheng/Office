import os
import os.path
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter,process_pdf
from pdfminer.converter import PDFPageAggregator,TextConverter
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from Office.save_file import save_to_text
from Office.get_path import getPath
from urllib.request import urlopen
from io import StringIO,open

def read_pdf(pdffile):
    fp = open(pdffile, 'rb')
    praser = PDFParser(fp)
    doc = PDFDocument()
    praser.set_document(doc)
    doc.set_parser(praser)
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    count = 1
    filecontent = []
    for page in doc.get_pages():
        interpreter.process_page(page)
        layout = device.get_result()
        countpage = '第%d页'%count
        count+=1
        pagecontent = []
        for x in layout:
            if (isinstance(x, LTTextBoxHorizontal)):
                results = x.get_text()
                print(results)
                pagecontent.append(results)
        filecontent.append({countpage:pagecontent})
    return filecontent


def read_onlinePDF(link):
    pdfFile = urlopen(link)
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    process_pdf(rsrcmgr, device, pdfFile)
    device.close()
    content = retstr.getvalue()
    retstr.close()
    return content

# data = read_pdf(r'C:\Users\Administrator\Desktop\量化投资资料\量化教材\Hands－On_Machine_Learning_for_Algorithmic_Trading.pdf')
# print(data)
# save_to_text('test',data[0]['第1页'])
