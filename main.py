import gspread
from google.oauth2.service_account import Credentials
import os

from dotenv import load_dotenv
load_dotenv()

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]

creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)

client = gspread.authorize(creds)

sheet_id = os.getenv("SHEET_ID")

workbook = client.open_by_key(sheet_id)

# values_list = sheet.sheet1.row_values(1)
sheet = workbook.worksheet("Sheet1")
sheet.update_acell("B3","Hello World")