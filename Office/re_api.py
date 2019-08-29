import re

##匹配邮箱
res = re.match('\w{4,20}@163\.com','laowang@163.comm')
print(res.group())

##多方式进行分割
s = "1+2-3"
a=re.split("[+-]",s)

##多个空格分割
re.split(r'\s+', 'a b   c')



sentence='''Hi Jack:
      Python is a beautiful language
      BR'''
patt=re.compile(r'(BR|Bestregards)$')
m=re.search(patt,sentence)
print(m.group())

match = re.sub(r'a', 'b','aaccaa')   # 把字符串中的a都替换为b


# res = re.findall(r'\[ \d{1,3} \](.*?)\[ \d{1,3} \]',txt,re.S)
# #print(res[2])
# for r in res:
#     print(len(r))
# patt=re.compile(r'^Chapter \d{1,2}')
# m=re.search(patt,txt)
# print(m)

# res = re.findall('^Chapter \d{1,2}$',txt)
# print(len(res))
# print(re.findall('^[\\u4e00-\\u9fa5]{0,}$',txt))



