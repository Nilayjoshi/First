import os
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_2.json'
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

spreadsheet_id = '1FqFhLDSlh7rcK322tk_Go_cf4dF-GGjbHd_aPkKkbHQ'
mySpreadsheets = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()

worksheet_name = 'Sheet1!'
cell_range_insert = 'F11'
values = (
    ('Deep')
)
value_range_body = {
    'majorDimension' : 'ROWS',
    'values': values
}

service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id,
    valueInputOption='USER_ENTERED',
    range=worksheet_name + cell_range_insert,
    body=value_range_body
).execute()


"""
gc = gspread.service_account(filename='python-first.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1FqFhLDSlh7rcK322tk_Go_cf4dF-GGjbHd_aPkKkbHQ/edit#gid=0')
scope = ['https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive","https://www.googleapis.com/auth/drive.readonly"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('python-first.json', scope)
client = gspread.authorize(credentials)

sheet = client.open("Test1").sheet1

ws = sh.worksheet('Sheet1')
df2 = pd.DataFrame(ws.get_all_records())

df2.to_csv('Test1.csv',index=False)
#print(df2)

df = pd.read_csv('Test1.csv')
sheet.update([df.columns.values.tolist()] + df.values.tolist())
"""