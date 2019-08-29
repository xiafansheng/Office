import pandas as pd

def csv_to_excel(csvpath):
    df = pd.read_csv(csvpath,error_bad_lines=False)
    name = csvpath.split(".")[0].split('\\')[-1]
    df.to_excel('%s.xlsx'%str(name),encoding='utf-8')
    print('%s转换成功'%name)
csv_to_excel(r'C:\Users\xfs9619\PycharmProjects\myprojct\Crawl\House\南昌二手房.csv')

