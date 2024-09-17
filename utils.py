from openpyxl import load_workbook

wb = load_workbook('bar.xlsx')
sheet = wb.active
#Про пиво
#Нужно переделать в функцию для снежения нагрузки
sheet1 =wb['Про пиво']

guinness = sheet1['A2'].value
guinness_info = sheet1['B2'].value
#guinness_detail = sheet1['C2'].value
#guinness_info = 'Про гиннесс'
guinness_detail = "Еще про гиннесс"

eventide= sheet1['A30'].value
eventide_info = sheet1['B30'].value
eventide_detail = sheet1['C30'].value

albion = sheet1['A4'].value
albion_info = sheet1['B4'].value
albion_detail = sheet1['C4'].value

ballantine_stout = sheet1['A3'].value
ballantine_stout_info = sheet1['B3'].value
ballantine_stout_detail = sheet1['C3'].value

black_sheep = sheet1['A25'].value
black_sheep_info = sheet1['B25'].value
black_sheep_detail = sheet1['C25'].value

oconnor = sheet1['A18'].value
oconnor_info = sheet1['B18'].value
oconnor_detail = sheet1['C18'].value

nocturne = sheet1['A7'].value
nocturne_info = sheet1['B7'].value
nocturne_detail = sheet1['C7'].value