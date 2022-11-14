import re

from telegram import Update
from telegram.ext import CallbackContext



def start(update: Update , context: CallbackContext):
    update.message.reply_text('hello bitch! how are you?')
    
def reply(update: Update , context: CallbackContext):
    
    message = update.message
    
    match = re.findall(r'[а-яА-ЯёЁ]', message.text)
    
    if len(match) != 0 and not '!ru' in message.text:
        message.reply_text('dont use russian please')
        message.delete()
        
        
    

