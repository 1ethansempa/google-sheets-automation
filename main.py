import gspread
from google.oauth2.service_account import Credentials
import os

from dotenv import load_dotenv
load_dotenv()

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]

# Read more about gspread
# https://docs.gspread.org/en/v6.0.0/user-guide.html

creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)

client = gspread.authorize(creds)

sheet_id = os.getenv("SHEET_ID")

workbook = client.open_by_key(sheet_id)

# values_list = sheet.sheet1.row_values(1)
# sheet = workbook.worksheet("Sheet1")

# sheet.update_acell("B3","Hello World")

# sheet.format("A1", {"textFormat": {"bold": True}})

values = [
    ["Name", "Price", "Quantity"],
    ["Basketball", 29.99, 1],
    ["Jeans", 39.99, 4],
    ["Socks", 9.99, 10],
]

worksheet_list = map(lambda x: x.title, workbook.worksheets())

new_worksheet_name = "Values"

if new_worksheet_name in worksheet_list:
    sheet = workbook.worksheet(new_worksheet_name)
else:
    sheet = workbook.add_worksheet(title=new_worksheet_name, rows=10, cols=10)
    
sheet.clear()

"""
for i, row in enumerate(values):
    for j, cell in enumerate(row):
        sheet.update_cell(i + 1, j + 1, cell)   
 """

sheet.update(f"A1:C{len(values)}", values)
sheet.format("A1:C1", {"textFormat": {"bold": True}})

sheet.update_cell(len(values) + 1, 2, "=sum(B2:B4)")