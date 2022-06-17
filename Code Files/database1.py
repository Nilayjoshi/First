import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

scope = ['https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('python-first.json', scope)
client = gspread.authorize(credentials)

#sheet = client.create("FirstSheet")

#sheet.share("jnilay3@gmail.com", perm_type="user", role="writer")

sheet = client.open("FirstSheet").sheet1

df = pd.read_csv('dict1.csv')

sheet.update([df.columns.values.tolist()] + df.values.tolist())
