import random
#from Office.get_classmate import get_field

def get_random(list,number):
    select = random.sample(set(list), number)
    return select

# info = get_field( ['姓名','性别'])
# boy = info[info['性别']=='男']['姓名'].values
# boy = [i for i in boy if i != '阮志朋' or '魏鑫']
# print(get_random(boy, 8))
