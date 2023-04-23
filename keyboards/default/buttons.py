from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton
from functions.convertorvalut import getcurrencysmybols
from keyboards.default.utils import build_inline_menu


# генерация кнопки главного меню
def generatemainmenu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(text='⛅️ Погода'),
               KeyboardButton(text='💰 Конвертер валют'),
               KeyboardButton(text='🖼️ Милые животные'),
               KeyboardButton(text='☑️ Опрос')
               )
    return markup


# генерация кнопку 'назад'

def backbutton():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('⬅️ Назад'))
    return markup


# генерация кнопки 'Картинки'

def animalsbutton():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(text='🖼️ Картинки'))
    markup.add(KeyboardButton('⬅️ Назад'))
    return markup


# генерация кнопки опроса
def generatetypepoll():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(text='QUIZ'), KeyboardButton(text='REGULAR'))
    markup.add(KeyboardButton('⬅️ Назад'))
    return markup
