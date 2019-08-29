# -*- coding:utf-8 -*-
# import pandas as pd
# import tabula
# data = tabula.read_pdf(r"C:\Users\Administrator\Desktop\Tariff List-09.17.18.pdf",encoding = 'utf-8',pages='all')
# data.to_excel('Tariff List-09.17.18.xls',encoding='gbk')

# def readpdf(name, page):
#     data = tabula.read_pdf(r"C:\Users\Administrator\Desktop\%s"%name, encoding='utf-8', pages=page)  # 'all' [1,2] 1
#     data.to_excel('%s.xls'%name, encoding='utf-8')
#     return '%s已经转为Excel文件'%name
#
#     # name = ['005经济学院', '007法学院', '008文化与传媒学院', '011政府管理学院', '013社会与心理学院', '017体育经济与管理学院', '019财经研究院', '020国防经济与管理研究院', '021中国经济与管理研究院（更新待定专业）', '022中国金融发展研究院', '023中国公共财政与政策研究院', '024人力资本与劳动经济研究中心', '027外国语学院', '029统计与数学学院（更新待定专业）', '031国际文化交流学院']
# def mmexcel(number,na):
#     x = tuple(range(number))
#     x = [pd.read_excel(r'C:\pycharm project\%s%d.xls'%na%i) for  i in range(1,number+1)]
#     data = pd.concat(list(x))
#     data.to_excel('merged%s.xls'%na,encoding='utf-8')
#     return '合并成功'

# a,b,c,d,e,f,g,h,i,j,k,l,m,n,o= [pd.read_excel(r'C:\pycharm project\%s%d.xls'%na%i) for  i in range(1,number+1)]
# data = pd.concat([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o])
# data.to_excel('admitted student.xls',encoding='utf-8')
# for i in range(1,7):
from tabula import wrapper
# data = wrapper.read_pdf("http://gs.cufe.edu.cn/system/resource/storage/download.jsp?mark=REE2MkE4Q0M2QzAwRjRDRjI0Q0JFRTJFRDAyOTk0MzcvMDMxNDc5RDQvOUFEMQ== ")
# print(data)


import PyPDF2
from tabula import wrapper
from Office.save_file import save_dfto_csv
# import tabula
#
pdfpath = r"C:\Users\xfs9619\Desktop\附件1 中央财经大学2019-2020学年第一学期研究生课程表（公共课部分）\中央财经大学2019-2020学年第一学期研究生课程表（学生专用）.pdf"
reader = PyPDF2.PdfFileReader(open(pdfpath, mode='rb' ))

n = reader.getNumPages()
df = []
for page in range(18,264):
    try:
        d = wrapper.read_pdf(pdfpath, pages=page)
        dfs = d.set_index(d['时间']).drop(columns=['时间','Unnamed: 0']).stack().reset_index()
        dfs.columns = ['节数', '星期', '课程信息']
        dfs = dfs.dropna(how='any')
        dfs['课程名称']= dfs['课程信息'].apply(lambda x:x.split('\r')[0])
        dfs['时间范围']= dfs['课程信息'].apply(lambda x:x.split('\r')[1])
        dfs['地点']= dfs['课程信息'].apply(lambda x:x.split('\r')[2])
        save_dfto_csv('课表',dfs)
        #res = dfs.drop(columns='课程信息')
        # df.append(d)
        # d.to_excel('%d.xlsx')
        print(str(page) + 'success')
    except:
        print(str(page)+'fail')

#
# df = []
# for page in [str(i+1) for i in range(n)]:
#     if page :
# #             df.append(read_pdf(r"C:\Users\riley\Desktop\Bank Statements\50340.pdf", area=(530,12.75,790.5,561), pages=page))
# #     else:
# #             df.append(read_pdf(r"C:\Users\riley\Desktop\Bank Statements\50340.pdf", pages=page))