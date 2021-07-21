import gspread
import pandas

""" Gestion de contenidos """
#Añadir nuevos retos y programas
#Eliminar retos y programas

""" Lectura de contenidos """
#Mostrar las categorias (ej: webscraping, hacking, etc...)
#Mostrar los programas organizados por categoria (solo nombre)
#Mostrar los detalles del programa

gc = gspread.service_account(filename="credentials/database.json")
key = open("credentials/key_drive_google.txt").read()


def showidprograms(category, gc=gc, key=key):
    
    sh = gc.open_by_key(key)
    program_sheet = sh.sheet1
    list_of_dicts = program_sheet.get_all_records()

    category_programs = program_sheet.col_values(5)
    if str(category) in category_programs:
        search = ""
        for program in list_of_dicts:
            if category == program["AREA"]:
                id = program["ID"]
                name = program["NOMBRE"]
                search = (search + f"\n>▪️ID:{id} Reto:{name}")
        return search
    else:
        return "Aun no existe esta categoria..."
    
def detailprogram(id, gc=gc, key=key):
    "Tomar un programa de la db si existe y retornarla"
    
    sh = gc.open_by_key(key)
    program_sheet = sh.sheet1
    
    id = id + 1

    id_programs = program_sheet.col_values(1)
    if str(id) in id_programs:
        program = program_sheet.row_values(int(id))
        
        id = program[0]
        title = program[1]
        level = program[2]
        details = program[3]
        category = program[4]
        
        texto = (f"<b>🔸{title}🔸</b>\n\n"
            f"{details}\n\n"
            f"<b>Categoria:</b> <code>{category}</code>\n"
            f"<b>Dificultad:</b> <code>{level}</code>\n"
            f"<b>ID:</b> <code>{id}</code>\n")

        return texto
    else:
        program = ("😅 Este programa aun no ha sido creado.")
    return program


def generar_ranking(): #Esta funcion aun esta en desarrollo

    """ generar_ranking(): lee una libro de google sheet, coje los datos, y los formatea para presentarlos en telegram
    """

    # abrir google sheet
    gc = gspread.service_account(filename="credentials/database.json")
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


