import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google_api import *
from Google import Create_Service

#from Client_data import info

"""
company = "ABC"
print(info(company))
"""

def info(company_name, spreadsheet_id, service, workbook, sheet, sheetname = 'Master'):
	exceldata = pd.read_excel("Client.xlsx")                                                                            
	dfdata = pd.DataFrame(exceldata)
	i = 0
	up1=[]
	up2=[]
	up3=[]

	for j in range(1,8):
		value = dfdata.iloc[0][i] 
		value = str(value)
		if j == 4:
			up2 = ({'range' : sheetname + '!' + 'B' + '3', 'values' : [[value]]}) #FOR COMPANY NAME
		elif j == 3:
			up3 = ({'range' : sheetname + '!' + 'B' + '10', 'values' : [[value]]}) #FOR PHONENUMBER
		up1 = ({'range' : sheetname + '!' + 'E' + '15', 'values' : [[value]]}) #FOR SUBSCRIPTION YEAR
		i+=1

	print(up1, up2, up3)
	for k in range(1,4):
		if k == 1:
			batch_update_values_request_body = {
				'value_input_option': 'USER_ENTERED',
				'data': up1,	
    		}
			request = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id, body=batch_update_values_request_body)
			response = request.execute()
		elif k==2:
			batch_update_values_request_body = {
				'value_input_option': 'USER_ENTERED',
				'data': up2,	
    		}
			request = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id, body=batch_update_values_request_body)
			response = request.execute()	
		else:
			batch_update_values_request_body = {
				'value_input_option': 'USER_ENTERED',
				'data': up3,	
    		}
			request = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id, body=batch_update_values_request_body)
			response = request.execute()	
			













"""
	up2=[]
	i=0
	
	for j in range(65,69):
		value = dfdata.iloc[20][i] #for company name
		value = str(value)
		up2 = ({'range' : sheetname + '!' + 'B' + '3', 'values' : [[value]]})
		i+=1

	batch_update_values_request_body = {
		'value_input_option': 'USER_ENTERED',
		'data': up2,
    }
	request = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id, body=batch_update_values_request_body)
	response = request.execute()
	return 1
"""	