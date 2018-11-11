from secrets import *
from variables import *
from telegram.ext import MessageHandler, Filters, Updater, CommandHandler, CallbackQueryHandler
import telegram
from telegram import bot, InlineKeyboardButton, InlineKeyboardMarkup
import json
import People_list

updater = Updater(token=secret_token)
dispatcher = updater.dispatcher

global lists
lists = []


import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
  level=logging.INFO)


def button(bot, update):
  query = update.callback_query
  switcher = {
      '1': "user_add_list",
      '2': "print_lists",
      '3': "select_list",
      '4': "add_member",
      '5': "show_members",
  }
  action = switcher.get(query.data,"error")

  bot.edit_message_text(text="Action => : {}".format(action),
    chat_id=query.message.chat_id,
    message_id=query.message.message_id)

def start(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text="welcome_text")
  

def add_member(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text=add_member_text)

def del_member(bot, update):
  bot.send_message(chat_id=update.message.chat_id, text=del_member_text)


def show(bot, update):
  keyboard = [[InlineKeyboardButton("Nova llista", callback_data='1'),
    InlineKeyboardButton("Mostra llista", callback_data='2')],
    [InlineKeyboardButton("afegir algú", callback_data='3'),
    InlineKeyboardButton("Eliminar algú ", callback_data='4')]]
  reply_markup = InlineKeyboardMarkup(keyboard)
  user = update.message.from_user
 

start_handler = CommandHandler('start', start)
add_member_handler = CommandHandler('add_member', add_member)
del_member_handler = CommandHandler('del_member', del_member)
show_handler = CommandHandler('show', show)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(add_member_handler)
dispatcher.add_handler(del_member_handler)
dispatcher.add_handler(show_handler)
dispatcher.add_handler(CallbackQueryHandler(button))

def new_list(bot, update, args):
    new_list = People_list(args)
    lists.append(new_list)
    bot.send_message(chat_id=update.message.chat_id, text="New list")
    for arg in args:
        print(arg)

def add_members(bot, update):
  print ("Hello")

def show_members(bot, update):
  print ("Hello")

def show_lists(bot, update):
      print ("Hello")

def Select_list(bot, update):
  print ("Hello")



new_list_handler = CommandHandler('new_list',new_list,pass_args=True)
show_lists_handler = CommandHandler('show_lists',show_lists)
Select_list_handler = CommandHandler('Select_list',Select_list)
add_members_handler = CommandHandler('add_members',add_members)
show_members_handler = CommandHandler('show_members',show_members)

dispatcher.add_handler(new_list_handler)
dispatcher.add_handler(show_lists_handler)
dispatcher.add_handler(Select_list_handler)
dispatcher.add_handler(add_members_handler)
dispatcher.add_handler(show_members_handler)


updater.start_polling()
