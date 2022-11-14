import random
import re

from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update , context: CallbackContext):
    update.message.reply_text('hello bitch! how are you?')
    
def reply(update: Update , context: CallbackContext):
    
    responses = [
        'котунду айрып алам нахуй',
        'буттучу заебал',
        'мен сага эмне баклажан корунуп турамбы?',
        'сенден косяк кетти',
        'ташагынды алмаштыра тебем',
        'бля, заебал cигилчи нахуй!',
        'амын айрылатко',
        'негирлер сигип кетсин',
        'жалап экенсин негизи',
        'бугун сен мал экенин белгилу',
        'коток соргонду жакшы коросунбу?',
        'тозоко туш',
        'олп кет',
        'бугун гейсин',
        'экинчи антпе',
        'сага каргыш тийди',
        'заебалкенсин блять',
        'качантан бери ушунча чычкак болуп калгансын?'
    ]
    
    message = update.message
    user = update.effective_user
    chat_id = update.message.chat_id
    response = responses[random.randint(0, len(responses)-1)]
    match = re.findall(r'[а-яА-ЯёЁ]', message.text)
    
    if len(match) != 0 and not '!ru' in message.text:
        # message.reply_text(f'{user.first_name}, {response}')
        context.bot.send_message(chat_id=chat_id, text=f'{user.first_name}, {response}')
        message.delete()
        
        
    

