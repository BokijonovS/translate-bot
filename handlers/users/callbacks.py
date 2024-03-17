from data.loader import bot, db
from telebot.types import Message, CallbackQuery
from translate import Translator

from keyboards.inline import languages_buttons

@bot.callback_query_handler(func=lambda call: call.data == 'translate')
def reaction_to_translate(call: CallbackQuery):
    chat_id = call.message.chat.id
    bot.delete_message(chat_id, call.message.message_id)
    bot.send_message(chat_id, 'Tilni tanlang', reply_markup=languages_buttons())

langs = {}

@bot.callback_query_handler(func=lambda call:call.data in ['uz_en', 'uz_ru', 'en_uz', 'en_ru', 'ru_en', 'ru_uz'])
def reaction_to_langs(call: CallbackQuery):
    chat_id = call.message.chat.id
    from_user_id = call.from_user.id
    from_lang, to_lang = call.data.split('_')
    langs[from_user_id] = {
        'from_lang': from_lang,
        'to_lang': to_lang
    }
    bot.delete_message(chat_id, call.message.message_id)
    msg = bot.send_message(chat_id, 'Tarjima uchun soz kiriting')
    bot.register_next_step_handler(msg, get_text)
def get_text(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    from_lang = langs[from_user_id]['from_lang']
    to_lang = langs[from_user_id]['to_lang']
    text = message.text

    translator = Translator(from_lang=from_lang, to_lang=to_lang)
    translation = translator.translate(text)
    bot.send_message(chat_id, translation)
    bot.send_message(chat_id, 'Tillar', reply_markup=languages_buttons())
