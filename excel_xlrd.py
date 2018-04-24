# coding:utf8
import xlrd
import xlwt

def read_excel():
    #open workbook
    book = xlrd.open_workbook('text.xlsx')

    #get all sheet name
    print(book.sheet_names())
    
    #sheet context
    table = book.sheet_by_name('Sheet1')
    #table = book.sheet_by_index(0)

    #nrows is the number of rows, row_values is row's value
    for i in range(table.nrows):
        print(table.row_values(i))

    #ncols is the number of cols, col_values is col's value
    for j in range(table.ncols):
        print(table.col_values(j)) 

    #get cell
    for i in range(1,table.nrows):
        for j in range(table.ncols):
            print(table.cell(i,j).value)

read_excel()        
