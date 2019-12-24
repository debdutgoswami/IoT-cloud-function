import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

def update(request):
    #geting the variables ready
    data = {
        #your client_json contents as dictionary
    }

    request_json = request.get_json()
    request_args = request.args
    temp,humidity = ""

	if request_json and 'temp' in request_json:
        temp = request_json['temp']
    elif request_args and 'temp' in request_args:
        temp = request_args['temp']

    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_dict(data,scope)

    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("Temperature").sheet1

    row = [datetime.now().strftime("%d/%m/%Y %H:%M:%S"), temp]
    index = 2
    sheet.insert_row(row, index)
