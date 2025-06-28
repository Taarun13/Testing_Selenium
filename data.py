from openpyxl import Workbook
from datetime import datetime, timedelta

wb = Workbook()
sheet = wb.active
sheet.title = "Flight Data"

sheet.append(["From", "To", "Date", "Passengers", "Airline"])

sample_data = [
    ("Chennai", "Delhi", datetime.today() + timedelta(days=10), 1, "Indigo"),
    ("Mumbai", "Bangalore", datetime.today() + timedelta(days=12), 2, "Air India"),
    ("Hyderabad", "Kolkata", datetime.today() + timedelta(days=15), 3, "SpiceJet"),
    ("Pune", "Chennai", datetime.today() + timedelta(days=18), 1, "Vistara"),
    ("Delhi", "Goa", datetime.today() + timedelta(days=20), 2, "Akasa Air"),
]

for row in sample_data:
    sheet.append([row[0], row[1], row[2].date(), row[3], row[4]])

wb.save("data.xlsx")
print("Excel file 'data.xlsx' created successfully.")
