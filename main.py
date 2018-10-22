from secrets import *
from variables import *
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters
import telegram
from telegram import bot
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup

updater = Updater(token=secret_token)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
  level=logging.INFO)


def button(bot, update):
  query = update.callback_query
  switcher = {
    "1": "afegeix-me" 
  }
  action = switcher.get(query.data,"error")

  bot.edit_message_text(text="Action => : {}".format(action),
    chat_id=query.message.chat_id,
    message_id=query.message.message_id)

def start(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text=welcome_text)

def add_member(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text=add_member_text)

def del_member(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text=del_member_text)


def show_list(bot, update):
  keyboard = [[InlineKeyboardButton("👍", callback_data='1'),
    InlineKeyboardButton("⛔", callback_data='2')],
    [InlineKeyboardButton("Treure algú altre ⛔", callback_data='3'),
    InlineKeyboardButton("Afegir algú altre 👍 ", callback_data='4')]]
  reply_markup = InlineKeyboardMarkup(keyboard)
  update.message.reply_text('T\'hi afegeixes?', reply_markup=reply_markup)

start_handler = CommandHandler('start', start)
add_member_handler = CommandHandler('add_member', add_member)
del_member_handler = CommandHandler('del_member', del_member)
show_list_handler = CommandHandler('show_list', show_list)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(add_member_handler)
dispatcher.add_handler(del_member_handler)
dispatcher.add_handler(show_list_handler)
dispatcher.add_handler(CallbackQueryHandler(button))


updater.start_polling()
