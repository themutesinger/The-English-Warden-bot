import random
import re

import translators as ts
from telegram import Update
from telegram.ext import CallbackContext


def reply(update: Update, context: CallbackContext):

    responses = [
        'больше так не делай',
        'ты должен умереть',
        'ты попадешь в ад'
    ]

    message = update.message
    user = update.effective_user
    chat_id = update.message.chat_id
    response = responses[random.randint(0, len(responses)-1)]
    match = re.findall(r'[а-яА-ЯёЁ]', message.text)

    if message.text[0] == '.':
        if len(match) != 0:
            traslate = ts.yandex(message.text[1:])
        else:
            traslate = ts.yandex(message.text[1:], to_language='ru')
        context.bot.send_message(chat_id=chat_id, text=f'Translate: {traslate}')

    elif len(match) != 0 and not '!' in message.text:
        context.bot.send_message(
            chat_id=chat_id, text=f'{user.first_name}, {response}')
        message.delete()
