from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def translate_button():
    markup = InlineKeyboardMarkup()

    btn1 = InlineKeyboardButton('Translate', callback_data='translate')
    markup.add(btn1)
    return markup

def languages_buttons():
    markup = InlineKeyboardMarkup()

    uz_en = InlineKeyboardButton('Uz-En', callback_data='uz_en')
    uz_ru = InlineKeyboardButton('Uz-Ru', callback_data='uz_ru')
    en_uz = InlineKeyboardButton('En-Uz', callback_data='en_uz')
    en_ru = InlineKeyboardButton('En-Ru', callback_data='en_ru')
    ru_en = InlineKeyboardButton('Ru-En', callback_data='ru_en')
    ru_uz = InlineKeyboardButton('Ru-Uz', callback_data='ru_uz')

    markup.add(uz_en, uz_ru, en_uz, en_ru, ru_en, ru_uz)
    return markup

