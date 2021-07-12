import gspread
import pandas
#test
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

    # abrir google sheet
    gc = gspread.service_account(filename="credentials/bd-sheet.json")
    key = open("credentials/key_drive_google.txt").read()
    wks = gc.open_by_key(key)

    # leer datos de la primera hoja
    worksheet = wks.get_worksheet(0)
    
    data = worksheet.get_all_values()
    # las dos primeras filas no contienen nada, por tanto eliminar
    del data[0:2]

    # leer las cabeceras
    headers = data.pop(0)
    # convertir a un dataframe de pandas
    df = pandas.DataFrame(data, columns=headers)
    # como todo es texto, convertir a entero la columna de los puntos
    df['Puntos Acumulados'] = df['Puntos Acumulados'].astype(int)
    # ordenar por puntos acumulados descendente y de paso elimnar el resto de las columnas
    ranking=df.sort_values(["Puntos Acumulados"], ascending=False)[["Nombre","Puntos Acumulados"]]
    # convertir a lista para luego generar el Markdown
    ranking=ranking.values.tolist()

    texto_mostrar = ""
    # Generar el Markdown con el nombre en negrita los puntos en cursiva
    for p in ranking:
        texto_mostrar += f"*{p[0]}* con _{p[1]} puntos_.\n"

    return texto_mostrar