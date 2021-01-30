import gspread
import pandas

def programs_weekly():
    
    gc = gspread.service_account(filename="credentials/bd-sheet.json")
    key = open("credentials/key_drive_google.txt").read()
    sh = gc.open_by_key(key)
    
    worksheet = sh.sheet1
    re = worksheet.get_all_values()
    
    return(re)

def generar_ranking():
    """ generar_ranking(): lee una libro de google sheet, coje los datos, y los formatea para presentarlos en telegram
    """

    gc = gspread.service_account(filename="credentials/bd-sheet.json")
    key = open("credentials/key_drive_google.txt").read()
    wks = gc.open_by_key(key)

    worksheet = wks.get_worksheet(0)
    
    data = worksheet.get_all_values()
    del data[0:2]

    headers = data.pop(0)
    df = pandas.DataFrame(data, columns=headers)
    df['Puntos Acumulados'] = df['Puntos Acumulados'].astype(int)
    ranking=df.sort_values(["Puntos Acumulados"], ascending=False)[["Nombre","Puntos Acumulados"]]
    ranking=ranking.values.tolist()

    texto_mostrar = ""
    for p in ranking:
        texto_mostrar += f"*{p[0]}* con _{p[1]} puntos_.\n"

    return texto_mostrar