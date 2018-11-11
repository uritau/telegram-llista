from secrets import *
from variables import *
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler, StringRegexHandler
import telegram
import json
import re
from telegram import bot

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
  level=logging.INFO)
logger = logging.getLogger(__name__)

user_list = []

def echo(bot, update):
  update.message.reply_text("Bot name {}".format(bot_name))
  
def add_member(bot, update):
  user_to_add = re.sub(r'\+\s|\+|\/add_member+\s','',update.message.text)
  user_list.append(user_to_add)
  print ("{}".format("user to add: {}".format(user_to_add)))
  update.message.reply_text("<b>{}</b> afegit a la llista!!!\n Apuntats: \n- {}".format(user_to_add,"\n- ".join(user_list)),parse_mode=telegram.ParseMode.HTML)

def del_member(bot, update):
  user_to_del = re.sub(r'\-\s|\-|\/add_member+\s','',update.message.text)
  print ("{}".format("user to del: {}".format(user_to_del)))
  user_list.remove(user_to_del)
  update.message.reply_text("<b>{}</b> tret de la llista!! :(  \nApuntats: \n- {}".format(user_to_del,"\n- ".join(user_list)),parse_mode=telegram.ParseMode.HTML)


def show(bot, update):
  print("show: user-list: {}".format(user_list))
  update.message.reply_text("users in list: {}".format(user_list))

def error(bot, update, error):
  logger.warning('Update "%s" caused error "%s"', update, error)

def main():
  updater = Updater(token=secret_token)
  dispatcher = updater.dispatcher

  dispatcher.add_error_handler(error)
  dispatcher.add_handler(RegexHandler(r'^\+', add_member))
  dispatcher.add_handler(RegexHandler(r'^\-', del_member))
  dispatcher.add_handler(RegexHandler(r'^show', show))
  dispatcher.add_handler(CommandHandler("echo", echo))
  
  updater.start_polling()

  updater.idle()

if __name__ == '__main__':
  main()