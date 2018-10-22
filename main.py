from secrets import *
from variables import *
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

updater = Updater(token=secret_token)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=welcome_text)

def add_member(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=add_member_text)

def del_member(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=del_member_text)


start_handler = CommandHandler('start', start)
add_member_handler = CommandHandler('add_member', add_member)
del_member_handler = CommandHandler('del_member', del_member)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(add_member_handler)
dispatcher.add_handler(del_member_handler)


def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu


updater.start_polling()
