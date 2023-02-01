import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('secretKey.json', scope)

client = gspread.authorize(creds)

spreadsheet = client.open("Testing")

sheet1 = spreadsheet.worksheet("Sheet1")


# Read Data

#Read Cell
print(sheet1.cell(2,1).value)

#Write Cell
# sheet1.update_cell(2,1,"test")

# Read Row
# print(sheet1.row_values(2))

#Read Column
# print(sheet1.col_values(2))


# Access Multiple Sheets

# for sheet_obj in  spreadsheet.worksheets():  
#     sheet_name = sheet_obj.title
#     print(sheet_name)