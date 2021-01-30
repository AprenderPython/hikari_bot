import gspread

def programs_weekly():
    
    gc = gspread.service_account(filename="credentials/bd-sheet.json")
    key = open("credentials/key_drive_google.txt").read()
    sh = gc.open_by_key(key)
    
    worksheet = sh.sheet1
    re = worksheet.get_all_values()
    
    print(re)
programs_weekly()

    