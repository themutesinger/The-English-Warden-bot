from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

from config import TOKEN
from callbacks import *


def main():
    updater = Updater(token=TOKEN)
    dp = updater.dispatcher

    reply_handler = MessageHandler(Filters.text, reply)

    dp.add_handler(reply_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
