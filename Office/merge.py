import pandas as pd
from Office.get_path import getPath
mergefile = pd.read_csv(r'C:\\Users\\Administrator\\Desktop\\excel\\realreturn.csv',names = ['a','b','c'])
#print(mergefile)
f,n = getPath(r'C:\Users\Administrator\Desktop\excel')
fs = [i for i in f if 'CA' in i]
for i in fs:
    name = i[-9:]
    df = pd.read_csv(i,names=['a','d','c'])
    data = pd.merge(mergefile,df,how='right',on=['a','c'])
    data.to_csv(name)