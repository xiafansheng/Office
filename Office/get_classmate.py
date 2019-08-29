import pandas as pd
def get_field(li):
    path = r'C:\Users\Administrator\Desktop\学委\金融学硕18.xlsx'
    df = pd.read_excel(path)
    dfs = df[li]
    return dfs

df = get_field(['是否硕博', '性别','姓名'])
print(df[df['性别']=='女'])

#'学号', '专业', '姓名', '录取方式', '班级', '是否硕博', '性别', '身份证号'
