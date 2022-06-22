from Google import Create_Service

def create_drive_service():

	CLIENT_SECRET_FILE = 'client_secret_3.json'
	API_NAME = 'drive'
	API_VERSION = 'v3'
	SCOPES = ['https://www.googleapis.com/auth/drive']
	drive_service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
	return drive_service

def create_sheets_service():

	CLIENT_SECRET_FILE = 'client_secret_3.json'
	API_NAME = 'sheets'
	API_VERSION = 'v4'
	SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
	sheets_service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
	return sheets_service

def create_folder( drive_service, folderName, parentID = None):

	body = {
		'name': folderName,
		'mimeType': "application/vnd.google-apps.folder"
	}
	if parentID:
		body['parents'] = [parentID]
	root_folder = drive_service.files().create(body = body).execute()
	return root_folder['id']

def copy_file( drive_service, file_name, parent_id, source_id):

	file_metadata={
		'name' : file_name,
		'parents' : [parent_id]
	}
	file_prop = drive_service.files().copy(
		fileId = source_id,
		body = file_metadata
	).execute()
	return file_prop['id']

def sheet_to_excel(drive_service, spreadsheet_id):

	byteData = drive_service.files().export_media(
		fileId = spreadsheet_id,
		mimeType = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
	).execute()

	with open( 'trial'  + '.xlsx', 'wb') as f:
		f.write(byteData)
		f.close()

def sheet_to_excel_filepath( filepath, drive_service, spreadsheet_id):

	byteData = drive_service.files().export_media(
		fileId = spreadsheet_id,
		mimeType = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
	).execute()

	with open( filepath, 'wb') as f:
		f.write(byteData)
		f.close()


# drive_service = create_drive_service()
# sheet_service = create_sheets_service()
# client_name = "Monil Shah"
# company_name = "Finsync"
# folder_id = create_folder( drive_service, client_name, '16n-6iU1TaCSr4eirhbT9pLbE7bsMBajc')
# file_id = copy_file( drive_service, company_name, folder_id , '1oQBFZO3FsVpcFDgStf7568JCkQmUzOhA_ArMaaIRLXg')