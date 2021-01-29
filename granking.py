import gspread
import pandas

def sacar_ranking():

    gc = gspread.service_account("bot-telegram-302121-9269276f665c.json")
    wks = gc.open_by_key('1W4dxhCViCFgArafr1uuHSsutHIwFGscgwBORJidZ0Qk')

    worksheet = wks.get_worksheet(0)
    #dataframe = pandas.DataFrame(worksheet.get_all_values())

    data = worksheet.get_all_values()
    del data[0:2]

    headers = data.pop(0)
    df = pandas.DataFrame(data, columns=headers)
    df['Puntos Acumulados'] = df['Puntos Acumulados'].astype(int)
    ranking=df.sort_values(["Puntos Acumulados"], ascending=False)[["Nombre","Puntos Acumulados"]]
    print (ranking)
    print (type(ranking))
    ranking=ranking.values.tolist()

    texto_mostrar = ""
    for p in ranking:
        texto_mostrar += f"*{p[0]}* con _{p[1]} puntos_.\n"

    return texto_mostrar