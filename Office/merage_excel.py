import pandas as pd
from Office.get_path import getPath




def merge_excel(pathlist,filename):
    dfs = []
    for path in pathlist:
        dfs.append(pd.read_csv(path))
    df = pd.concat(dfs)
    df.to_excel('%s.xlsx' % filename)

f,n = getPath(r'C:\pycharm project\Crawl')
pathlist = [i for i in f if '数据' in i and '-' in i]
merge_excel(pathlist,'上海市交易所数据')