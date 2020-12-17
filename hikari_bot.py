import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

token = input("Ingresa el token del bot:-->")
updater = Updater(token=token, use_context=True)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola Humano")

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)

updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(echo_handler)

updater.start_polling()