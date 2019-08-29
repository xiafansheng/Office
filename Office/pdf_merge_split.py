from PyPDF2 import  PdfFileMerger,PdfFileWriter,PdfFileReader,pagerange
import re

def merge_pdf(firstpdf,secondpdf,insertpage):
    # 创建一个用来合并文件的实例
    pdf_merger = PdfFileMerger()
    pdf_merger.append(firstpdf)
    pdf_merger.merge(insertpage, secondpdf)
    # # 添加书签
    # pdf_merger.addBookmark('这是一个书签', 1)
    pdf_merger.write('merge_pdf.pdf')

#
# def split_by_num(filename, nums, password=None):
filename = r'F:\研一下\量化投资资料\量化教材\Hands－On_Machine_Learning_for_Algorithmic_Trading.pdf'
pdf_reader = PdfFileReader(open(filename, mode='rb' ))
pages = pdf_reader.getNumPages()
outline = pdf_reader.getOutlines()
outlinchapter = []
outlinepage = [i+18 for i in [8,33,65,88,119,147,175,224,260,284,312,351,389,418,441,458]]
for o in outline:
    res = re.findall(r"'/Title': '(.*?)', '/Page': IndirectObject\((.*?), 0\)",str(o),re.S)
    if 'Chapter' in res[0][0]:
        outlinchapter.append(res[0][0])
#print(list(outlinedict[0].keys())[0],list(outlinedict[0].values())[0])
outlinedict =[{i[0]:i[1]} for i in zip(outlinchapter,outlinepage)]


for i in range(len(outlinedict)+1):
    pdf_writer = PdfFileWriter()
    split_pdf_name = list(outlinedict[i].keys())[0].replace(':','') + '.pdf'
    start = list(outlinedict[i].values())[0]
    end = list(outlinedict[i+1].values())[0]
    print(split_pdf_name)
    for i in range(int(start), int(end)):
        pdf_writer.addPage(pdf_reader.getPage(i))
    with open(split_pdf_name,'wb') as out:
        pdf_writer.write(out)



