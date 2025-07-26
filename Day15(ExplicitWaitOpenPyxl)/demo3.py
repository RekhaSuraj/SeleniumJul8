import openpyxl

# openpyxl - openpyxl is a Python library to read/write Excel 2010 - xlsx/xlsm/xltx/xltm files
# open the excel file
wb = openpyxl.load_workbook('../data/Book1.xlsx')
# go to sheet
sheet = wb['Sheet1']

# go to first row
var = sheet.cell(1,1)
# cell.value - Get or set the value held in the cell
print(var.value)
# python

