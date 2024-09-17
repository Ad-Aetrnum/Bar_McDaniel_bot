from openpyxl import load_workbook

wb = load_workbook('bar.xlsx')
sheet = wb.active
sheet3 =wb['Про пиво']
name = sheet3['A2'].value
info = sheet3['B2'].value
detail = sheet3['C2'].value
print(name)
print(info)
print(detail)