#version: 1
# https://docs.gspread.org/en/latest/user-guide.html

from telegram.ext import Updater, CommandHandler, Filters, CallbackQueryHandler, ConversationHandler, CallbackContext
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, update
import telegram
import random

import functions

token = open("credentials/token.txt").read()
updater = Updater(token=token, use_context=True)

#Commands
def start(update, context):
    """ Saluda a hikari """
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    saludos = ("Hola Humano :)", "Holaa", "Aqui estoy 👋", "Hikari: On \n:b")
    context.bot.send_message(chat_id=update.effective_chat.id, text=random.choice(saludos))

def showcategories(update, context):
    """ Mostrar la lista de programas """

    
    category_botons = [
        [
            InlineKeyboardButton("Webscraping", callback_data='webscraping'),
            InlineKeyboardButton("Automatizacion", callback_data='automatizacion'),
            InlineKeyboardButton("Asistente", callback_data='Asistente'),
        ],[
            InlineKeyboardButton("Hacking", callback_data='hacking'),
            InlineKeyboardButton("OSINT", callback_data='osint'),
            InlineKeyboardButton("Criptografia", callback_data='cripto'), 
        ],[
            InlineKeyboardButton("Algoritmos", callback_data='algoritmos'),
            InlineKeyboardButton("Gestion de texto", callback_data='gestiontexto'),
            InlineKeyboardButton("Matematicos", callback_data='Matematicos'),  
        ],[
            InlineKeyboardButton("Asistente", callback_data='asistente'),
        ]
        ]

    reply_markup = InlineKeyboardMarkup(category_botons)

    update.message.reply_text('Selecciona una categoria: ', reply_markup=reply_markup)

def showall(update, context):
    category = " ".join(context.args)
    programs = functions.showidprograms(category)
    context.bot.send_message(chat_id=update.effective_chat.id, text=programs)



def showprogram(update, context):
    """ Mostrar los detalles de un programa en especifico """
    
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)

    #Tomar el argumento que el usuario escriba
    idprogram = " ".join(context.args)
    if idprogram.isdigit():
        programdetails = functions.detailprogram(id = int(idprogram))
    else:
        programdetails = (f"<b>ID no encontrado...</b> \n\n<b>Para usar esta funcion debe especificar el id correctamente:</b>\n\nEj: <code>/showp 1 </code>\n")
    context.bot.send_message(chat_id=update.effective_chat.id, text=programdetails, parse_mode=telegram.ParseMode.HTML)

def help(update, context):
    """Wiki de hikari """

    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=telegram.ChatAction.TYPING)
    help = (
    "Hola, mi nombre es hikari y aqui podras aprender a usarme :)\n\n"
    "Los comandos disponibles son:\n\n"
    "/start - Usame para saludarme y ver si estoy viva.\n"
    "/showc - Usame para ver las categorias de los retos de programacion\n"
    "/showall - Usame para ver todos las categorias de retos\n"
    "ej: /showall Redes (las categorias los ves con /showc)\n"
    "/showp - Usame para ver los detalles de algun programa\n"
    "ej: /showp 8  (los ids lo ves con /showall <categoria>)\n"
    "/help - Si tienes alguna duda podes volver aqui :)\n\n"
    "Cualquier duda o bug puedes reportarlo a @dark_zly o a la comunidad @aprenderpython"
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=help)

#Listeners 
start_handler = CommandHandler("start", start)
help_handler = CommandHandler("help", help)
showpcat_handler = CommandHandler("showc", showcategories, pass_args=True)
showpall_handler = CommandHandler("showall", showall, pass_args=True)
showprogram_handler = CommandHandler("showp", showprogram, pass_args=True)

updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(help_handler)
updater.dispatcher.add_handler(showpcat_handler)
updater.dispatcher.add_handler(showpall_handler)
updater.dispatcher.add_handler(showprogram_handler)

updater.start_polling()