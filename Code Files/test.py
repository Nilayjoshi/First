import gspread
import pandas as pd
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials

gc = gspread.service_account(filename='python-first.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1FqFhLDSlh7rcK322tk_Go_cf4dF-GGjbHd_aPkKkbHQ/edit#gid=0')
scope = ['https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('python-first.json', scope)
client = gspread.authorize(credentials)

#sheet = client.create("Test1")
#sheet.share("jnilay3@gmail.com", perm_type="user",role="writer")
sheet = client.open("Test1").sheet1


lst = []
for i in range(0,5):
    ele = input()
    lst.append(ele)
print(lst)

ws = sh.worksheet('Sheet1')
df2 = pd.DataFrame(ws.get_all_records())


df2.loc[len(df2)] = lst
print(df2)

#edit_dict={}
df2.to_csv('Test1.csv',index=False)

df = pd.read_csv('Test1.csv')
sheet.update([df.columns.values.tolist()] + df.values.tolist())

#print(df2.columns[3])