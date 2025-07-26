import openpyxl

wb = openpyxl.load_workbook('../data/Book2.xlsx')
sheet = wb['Sheet1']

for i in range(1,4):
    for j in range(1,4):
        var = sheet.cell(i,j).value
        print(var,end=" ")

    print()

# A1 B1 C1
# A2 B2 C2
# A3 B3 C3



