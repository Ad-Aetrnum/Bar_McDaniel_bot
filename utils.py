from openpyxl import load_workbook

wb = load_workbook('bar.xlsx')
sheet = wb.active
#Про пиво
#Нужно переделать в функцию для снежения нагрузки
sheet1 =wb['Про пиво']

def info_beer (name):
    if name == "guinness":
        info = sheet1['B2'].value
        detail = sheet1['C2'].value
    elif name == "albion":
        info = sheet1['B4'].value
        detail = sheet1['C4'].value
    elif name == "oconnor":
        info = sheet1['B18'].value
        detail = sheet1['C18'].value
    elif name == "ballantine_stout":
        info = sheet1['B3'].value
        detail = sheet1['C3'].value
    elif name == "nocturne":
        info = sheet1['B7'].value
        detail = sheet1['C7'].value
    elif name == "eventide":
        info = sheet1['B30'].value
        detail = sheet1['C30'].value
    elif name == "black_sheep":
        info = sheet1['B25'].value
        detail = sheet1['C25'].value
    else:
        info = 'No info'
        detail = 'No detail'
    return info, detail
