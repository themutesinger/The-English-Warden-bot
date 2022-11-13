from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

from config import TOKEN
from action import *


def main():
    updater = Updater(token=TOKEN)
    dp = updater.dispatcher

    start_handler = CommandHandler('start', start)
    reply_handler = MessageHandler(Filters.text, reply)

    dp.add_handler(start_handler)
    dp.add_handler(reply_handler)
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
