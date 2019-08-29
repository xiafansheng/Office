from Office.get_path import getPath
import os
import pandas as pd

def get_stu_info(path,mode='id-name'):
    df = pd.read_excel(path)
    df = df.set_index('学号')
    df = df[df['是否硕博']==0]
    if mode == 'id-name':
        id_name = df['姓名'].to_dict()
        return id_name
    if mode == 'id-major':
        id_major = df['班级'].to_dict()
        return id_major


def get_name(filename):
    for k,v in id_name.items():
        try:
            if v in filename:
                return k,v
        except:
            print(filename,'not find name')


# def rename():
#     p,n =getPath(filepath)
#     for i in p:
#         try:
#             id,name = get_name(i)
#             major = id_major[id]
#             newfilename = r'C:\Users\Administrator\Desktop\attachment\%s-%s-%s.docx'%(name,major,id)
#             os.rename(i,newfilename)
#             print(i,'>>>',newfilename)
#         except:
#             print(i,'not convert ****',newfilename)

def submit_info(renamedfilepath):
    p, n = getPath(renamedfilepath)
    name = [get_name(i)[1] for i in p]
    submitednu = len(name)
    submitedlist = name
    needsubmitlist = [v for k,v in id_name.items()]
    needsubmitnu = len(needsubmitlist)
    notsubmitlist = [i for i in needsubmitlist if i not in submitedlist]
    notsubmitnu = len(notsubmitlist)
    return notsubmitnu,notsubmitlist


stu_path = r'C:\Users\Administrator\Desktop\学委\金融学硕18.xlsx'
filepath = r'C:\Users\Administrator\Desktop\attachment'
renamedfilepath = r'C:\Users\Administrator\Desktop\周一56节1班沙河主教219'
id_name = get_stu_info(stu_path)
name_id = {v: k for k, v in id_name.items()}
id_major =  get_stu_info(stu_path,mode='id-major')
p, n = getPath(filepath)
for i in p:
    try:
        id, name = get_name(i)
        major = id_major[id]
        title = '%s-%s-%s'% (name, major, id)
        if i.endswith('doc'):
            newfilename = r'C:\Users\Administrator\Desktop\周一56节1班沙河主教219\%s.doc' % title
        if i.endswith('docx'):
            newfilename = r'C:\Users\Administrator\Desktop\周一56节1班沙河主教219\%s.docx' % title
        if i.endswith('pdf'):
            newfilename = r'C:\Users\Administrator\Desktop\周一56节1班沙河主教219\%s.pdf' % title
        os.rename(i, newfilename)
    except:
        print(i)

notsubmitnu,notsubmitlist = submit_info(renamedfilepath)
print(notsubmitnu)
for i in sorted(notsubmitlist):
    print(i,name_id[i])
