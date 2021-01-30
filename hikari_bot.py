#version:0.1
"""
Alias del bot: @LordHikariBot

Ayuda:
https://python-telegram-bot.readthedocs.io/en/stable/
https://docs.google.com/spreadsheets/d/1W4dxhCViCFgArafr1uuHSsutHIwFGscgwBORJidZ0Qk/edit#gid=0
"""

from telegram.ext import Updater, CommandHandler, Filters
import functions

token = "" #aqui falta leer el token
updater = Updater(token=token, use_context=True)

#Commands
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola Humano")

#Listeners 
start_handler = CommandHandler('start', start)
updater.dispatcher.add_handler(start_handler)
updater.start_polling()