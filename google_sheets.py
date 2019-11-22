import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('secret_creds.json', scope)
client = gspread.authorize(creds)


sheet=client.open("Python Market Data").sheet1


cell = sheet.cell(1,2)

file=open("market_data.csv","r")


row=1
for line in file:
    l=line.split(",")
    cell_list = sheet.range('A{0}:F{0}'.format(row))

    j=0
    for cell in cell_list:
        cell.value = l[j]
        j+=1
    sheet.update_cells(cell_list)
    
    row+=1
