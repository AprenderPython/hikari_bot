#version:0.1
import logging
import random
from telegram.ext import Updater, CommandHandler, Filters

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

start_handler = CommandHandler('start', start)
random_temas = CommandHandler('rtemas', random_temas)

updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(random_temas)

updater.start_polling()
#https://python-telegram-bot.readthedocs.io/en/stable/