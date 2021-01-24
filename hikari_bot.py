#version:0.1
import logging
import random
from telegram.ext import Updater, CommandHandler, Filters

# funcion ranking
import gspread

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

token = input("Ingresa el token del bot:-->")
updater = Updater(token=token, use_context=True)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola Humano")

def random_temas(update, context):
    randomT = ["webscraping", "forense", "redes", "hacking", "criptografia"]
    randomT = random.sample(randomT, k=4)
    context.bot.send_message(chat_id=update.effective_chat.id, text=(randomT))
    print ("uno")

def ranking_s (update, context):
    gc = gspread.service_account('leer-googlesheet-bb4517f9acf2.json')
    sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/17LChMVFNgyQnAyodf1bHROlyA7x8GSHMV9l8sMhZokk/edit?usp=sharing')
    result_input = sht2.sheet1.get('A4:B5')
    
    texto_mostrar = ""
    for p in result_input:
        texto_mostrar += f"*{p[0]}* con _{p[1]} puntos_.\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=texto_mostrar, parse_mode="Markdown")
    

start_handler = CommandHandler('start', start)
random_temas = CommandHandler('rtemas', random_temas)
ranking_s = CommandHandler('ranking', ranking_s)

updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(random_temas)
updater.dispatcher.add_handler(ranking_s)

updater.start_polling()
#https://python-telegram-bot.readthedocs.io/en/stable/