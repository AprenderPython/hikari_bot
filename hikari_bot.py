#version: 1.0

from telegram.ext import Updater, CommandHandler
from telegram import update, ChatAction
from Functions.BasicFunctions import functions
import random

token = functions.config()
updater = Updater(token=token, use_context=True)

#Commands
def start(update, context):
    """ Saluda a hikari """
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    saludos = ("Hola Humano :)", "Holaa", "Aqui estoy 👋", "Hikari: On \n:b")
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(saludos))

def help(update, context):
    """Acerca de Hikari Bot"""
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    context.bot.send_message(chat_id=update.effective_chat.id, text=functions.help())

#Listeners 
start_handler = CommandHandler("start", start)
help_handler = CommandHandler("help", help)
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(help_handler)
updater.start_polling()