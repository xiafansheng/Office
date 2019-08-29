import xlrd

import pandas as pd
pd.pivot_table
xlsx = xlrd.open_workbook('d:/7月下旬入库表.xlsx')

table = xlsx.sheet_by_index(0)
# 通过sheet名查找：xlsx.sheet_by_name("7月下旬入库表")
# 通过索引查找：xlsx.sheet_by_index(3)
print(table.cell_value(0, 0))

# table.cell_value(1, 2)
# print(table.cell(1, 2).value)
# print(table.row(1)[2].value)



for i in range(0, xlsx.nsheets):
    table = xlsx.sheet_by_index(i)
    print(table.cell_value(0, 0))

# 获取所有sheet名字：xlsx.sheet_names()
# 获取sheet数量：xlsx.nsheets

for i in xlsx.sheet_names():
    table = xlsx.sheet_by_name(i)
    print(table.cell_value(3, 3))



import xlwt
new_workbook = xlwt.Workbook()
worksheet = new_workbook.add_sheet('new_test')
worksheet.write(0, 0, 'test')
new_workbook.save('d:/test.xls')


from xlutils.copy import copy
import xlrd
import xlwt

tem_excel = xlrd.open_workbook('D:/日统计.xls', formatting_info=True)
tem_sheet = tem_excel.sheet_by_index(0)

new_excel = copy(tem_excel)
new_sheet = new_excel.get_sheet(0)

style = xlwt.XFStyle()

font = xlwt.Font()
font.name = '微软雅黑'
font.bold = True
font.height = 360
style.font = font

borders = xlwt.Borders()
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
style.borders = borders

alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER
style.alignment = alignment

"""
new_sheet.write(2, 1, 12)
new_sheet.write(3, 1, 18)
new_sheet.write(4, 1, 19)
new_sheet.write(5, 1, 15)
"""

new_sheet.write(2, 1, 12, style)
new_sheet.write(3, 1, 18, style)
new_sheet.write(4, 1, 19, style)
new_sheet.write(5, 1, 15, style)


new_excel.save('D:/填写.xls')


import xlrd
import xlwt
from xlutils.copy import copy

xlsx = xlrd.open_workbook('d:/7月下旬入库表.xlsx')

table = xlsx.sheet_by_index(0)

all_data = []
for n in range(1, table.nrows):
    company = table.cell(n, 1).value
    price = table.cell(n, 3).value
    weight = table.cell(n, 4).value

    data = {'company': company, 'weight': weight, 'price': price}
    all_data.append(data)
# 以下内容可以用pandas的groupby轻易实现，这里不引入新知识，使用一个笨办法
a_weight = []
a_total_price = []
b_weight = []
b_total_price = []
c_weight = []
c_total_price = []
d_weight = []
d_total_price = []

for i in all_data:
    if i['company'] == '张三粮配':
        a_weight.append(i['weight'])
        a_total_price.append(i['weight'] * i['price'])
    if i['company'] == '李四粮食':
        b_weight.append(i['weight'])
        b_total_price.append(i['weight'] * i['price'])
    if i['company'] == '王五小麦':
        c_weight.append(i['weight'])
        c_total_price.append(i['weight'] * i['price'])
    if i['company'] == '赵六麦子专营':
        d_weight.append(i['weight'])
        d_total_price.append(i['weight'] * i['price'])


tem_excel = xlrd.open_workbook('D:/统计表_模板.xls', formatting_info=True)
tem_sheet = tem_excel.sheet_by_index(0)

new_excel = copy(tem_excel)
new_sheet = new_excel.get_sheet(0)

style = xlwt.XFStyle()

font = xlwt.Font()
font.name = '微软雅黑'
font.bold = True
font.height = 360
style.font = font

borders = xlwt.Borders()
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
style.borders = borders

alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER
style.alignment = alignment

new_sheet.write(2, 1, len(a_weight), style)
new_sheet.write(2, 2, round(sum(a_weight), 2), style)
new_sheet.write(2, 3, round(sum(a_total_price), 2), style)
new_sheet.write(3, 1, len(b_weight), style)
new_sheet.write(3, 2, round(sum(b_weight), 2), style)
new_sheet.write(3, 3, round(sum(b_total_price), 2), style)
new_sheet.write(4, 1, len(c_weight), style)
new_sheet.write(4, 2, round(sum(c_weight), 2), style)
new_sheet.write(4, 3, round(sum(c_total_price), 2), style)
new_sheet.write(5, 1, len(d_weight), style)
new_sheet.write(5, 2, round(sum(d_weight), 2), style)
new_sheet.write(5, 3, round(sum(d_total_price), 2), style)


new_excel.save('d:/7月下旬统计表.xls')



import xlrd
import xlwt
from xlutils.copy import copy
from Database import pymysql

database = pymysql.connect("127.0.0.1", "test", "test", "db", charset='utf8')

cursor = database.cursor()

sql = "SELECT company ,COUNT(company),SUM(weight),SUM(weight*price) FROM data  GROUP BY company"
cursor.execute(sql)
result = cursor.fetchall()
# print(result)
for i in result:
    if i[0] == '张三粮配':
        a_num = i[1]
        a_weight = i[2]
        a_total_price = i[3]
    elif i[0] == '李四粮食':
        b_num = i[1]
        b_weight = i[2]
        b_total_price = i[3]
    elif i[0] == '王五小麦':
        c_num = i[1]
        c_weight = i[2]
        c_total_price = i[3]
    elif i[0] == '赵六麦子专营':
        d_num = i[1]
        d_weight = i[2]
        d_total_price = i[3]

tem_excel = xlrd.open_workbook('D:/统计表_模板.xls', formatting_info=True)
tem_sheet = tem_excel.sheet_by_index(0)

new_excel = copy(tem_excel)
new_sheet = new_excel.get_sheet(0)

style = xlwt.XFStyle()

font = xlwt.Font()
font.name = '微软雅黑'
font.bold = True
font.height = 360
style.font = font

borders = xlwt.Borders()
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
style.borders = borders

alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER
style.alignment = alignment

new_sheet.write(2, 1, a_num, style)
new_sheet.write(2, 2, a_weight, style)
new_sheet.write(2, 3, a_total_price, style)
new_sheet.write(3, 1, b_num, style)
new_sheet.write(3, 2, b_weight, style)
new_sheet.write(3, 3, b_total_price, style)
new_sheet.write(4, 1, c_num, style)
new_sheet.write(4, 2, c_weight, style)
new_sheet.write(4, 3, c_total_price, style)
new_sheet.write(5, 1, d_num, style)
new_sheet.write(5, 2, d_weight, style)
new_sheet.write(5, 3, d_total_price, style)

new_excel.save('d:/7月下旬统计表.xls')
