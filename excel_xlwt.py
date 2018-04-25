# coding:utf8
# 只写入了首行，表格内容填充在爬虫脚步中完善

import xlwt

def excel_write_head():
    # build a workbook
    book = xlwt.Workbook(encoding = 'utf8')

    # build a sheet
    sheet = book.add_sheet('MySheet') 

    # head of the table
    head = ['名称', '分数', '类型', '片长', '语言']

    #write head
    col = 0
    for each_head in head:
        sheet.write(0, col, each_head)
        col += 1

    book.save('movie.xlsx')

excel_write_head()
