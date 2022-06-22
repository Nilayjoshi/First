import gspread
import pandas as pd
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
from google_api import *
from Google import Create_Service
from openpyxl import *
from info import info

gc = gspread.service_account(filename='python-first.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1qri2g0OcuHY3YxNvJ8jUOCjPEACmfWGSVT0M8wU_1Wc/edit#gid=0')
scope = ['https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('python-first.json', scope)
client = gspread.authorize(credentials)

#sheet = client.create("Finsync Solutions Inc.")
#sheet.share("jnilay3@gmail.com", perm_type="user",role="writer")
sheet = client.open("Finsync Solutions Inc.").sheet1
ws = sh.worksheet('Master')
df2 = pd.DataFrame(ws.get_all_values())
print(df2)

df2.to_csv('Finsync.csv',index=False)

sheets_service = create_sheets_service()
drive_service = create_drive_service()

spreadsheet_id = '1qri2g0OcuHY3YxNvJ8jUOCjPEACmfWGSVT0M8wU_1Wc'
company_name = 'Finsync Solutions Inc.'

sheet_to_excel(drive_service, spreadsheet_id)

filepath = 'trial.xlsx'
workbook = load_workbook(filename = filepath, data_only=True)

info(company_name, spreadsheet_id, sheets_service, workbook, sheet)