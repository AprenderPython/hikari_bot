#version:0.1
import logging
import random
from telegram.ext import Updater, CommandHandler, Filters

import gspread
import pandas
import granking as r

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#token = input("Ingresa el token del bot:-->")
token ="1572422104:AAHvIQesqhU-c_nhyFhA1U8lAEynh6HYdi0"
updater = Updater(token=token, use_context=True)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola Humano")

def random_temas(update, context):
    randomT = ["webscraping", "forense", "redes", "hacking", "criptografia"]
    randomT = random.sample(randomT, k=4)
    context.bot.send_message(chat_id=update.effective_chat.id, text=(randomT))
    print ("uno")

def ranking_s (update, context):
    # # gc = gspread.service_account('leer-googlesheet-bb4517f9acf2.json')
    gc = gspread.service_account("bot-telegram-302121-9269276f665c.json")

    # sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/17LChMVFNgyQnAyodf1bHROlyA7x8GSHMV9l8sMhZokk/edit?usp=sharing')
    sht2 = gc.open_by_key('1W4dxhCViCFgArafr1uuHSsutHIwFGscgwBORJidZ0Qk')

    result_input = sht2.sheet1.get('A4:D11')
    
    texto_mostrar = ""
    for p in result_input:
        texto_mostrar += f"*{p[0]}* con _{p[3]} puntos_.\n"

    #print (texto_mostrar) 
    context.bot.send_message(chat_id=update.effective_chat.id, text=(texto_mostrar), parse_mode="Markdown")
    

def bot_ranking (update, context):
    listado = r.sacar_ranking ()
    context.bot.send_message(chat_id=update.effective_chat.id, text=(listado), parse_mode="Markdown")

start_handler = CommandHandler('start', start)
random_temas = CommandHandler('rtemas', random_temas)
ranking_handler = CommandHandler('ranking', ranking_s)
ranking_handler2 = CommandHandler('ranking2', bot_ranking)

updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(random_temas)
updater.dispatcher.add_handler(ranking_handler)
updater.dispatcher.add_handler(ranking_handler2)

updater.start_polling()
#https://python-telegram-bot.readthedocs.io/en/stable/