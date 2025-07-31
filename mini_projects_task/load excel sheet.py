import openpyxl
wb = openpyxl.load_workbook("status.xlsx")
sheet = wb.active 
for row in sheet.iter_rows(min_row=2, values_only=True):
    print("Row Data:", row)
