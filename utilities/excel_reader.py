import openpyxl

def read_excel(file, sheet):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheet]

    data = []
    for row in sheet.iter_rows(values_only=True):
        data.append(row)

    return data