import json
import pandas as pd

def save_to_text(filename,variblelist):
    with open('%s'%filename, 'a+', encoding='utf-8',) as f:
        variblelist = [str(x) for x in variblelist]
        content = ';'.join(variblelist) + '\n'
        f.write(content)

def save_to_csv(filename,variblelist):
    df = pd.DataFrame([variblelist])
    #df.columns = headers
    df.to_csv('%s.csv'%filename, mode='a', header=False,encoding='GB18030')
    #csv_to_xls.csv_to_excel('%s'%filename)

def save_dfto_csv(filename,df):
    df.to_csv('%s.csv'%filename, mode='a', header=True,encoding='utf-8')
    #csv_to_xls.csv_to_excel('%s'%filename)

def save_to_json(filename,dictlist):
    file = '%s.json'%filename
    with open(file, 'a+',encoding='utf-8') as f:
        json.dumps(dictlist, f)
