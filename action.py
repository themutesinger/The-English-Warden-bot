import re

from telegram import Update
from telegram.ext import CallbackContext
from langdetect import detect, detect_langs
from langdetect import DetectorFactory
DetectorFactory.seed = 0


def start(update: Update , context: CallbackContext):
    update.message.reply_text('hello bitch! how are you?')
    
def reply(update: Update , context: CallbackContext):
    
    message = update.message
    
    match = re.findall(r'[а-яА-ЯёЁ]', message.text)
    
    
    if detect(message.text) == 'ru':
        update.message.reply_text('dont use russian please') 
        update.message.delete()
         
        
    elif len(match) != 0:
        message.reply_text('dont use russian please')
        message.delete()
        
    

