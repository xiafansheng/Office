import pandas as pd
from Office.get_path import getPath
from Office.save_file import save_dfto_csv

f,p = getPath(r'C:\Users\xfs9619\Desktop\附件1 中央财经大学2019-2020学年第一学期研究生课程表（公共课部分）')
# for nj in f:
#     print(nj)
    # sheet = pd.ExcelFile(nj).sheet_names
    # for zy in sheet[1:]:
    #     try:
    #         df = pd.read_excel(nj,sheet_name=zy)
    #         df = df.iloc[2:,1:]
    #         df.columns = ['节数']+['星期'+ str(i)  for i in range(1,8)]
    #         dfs = df.set_index(df['节数']).drop(columns='节数').stack().reset_index()
    #         dfs.columns = ['节数','星期','课程信息']
    #         dfs = dfs.dropna(how='any')
    #         dfs['课程名称']= dfs['课程信息'].apply(lambda x:x.split('\n')[0])
    #         dfs['时间范围']= dfs['课程信息'].apply(lambda x:x.split('\n')[1])
    #         dfs['地点']= dfs['课程信息'].apply(lambda x:x.split('\n')[-1])
    #         res = dfs.drop(columns='课程信息')
    #         res['专业'] = zy
    #         save_dfto_csv('kb',res)
    #         print(zy +'success')
    #     except:
    #         print(zy + 'error')

df = pd.read_csv('课表.csv')
df.to_excel('课表.xlsx')
ddf = df.drop_duplicates(subset=['节数','星期','地点'])
ddf.to_excel('去重课表.xlsx')
