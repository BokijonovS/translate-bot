from data.loader import bot, db
from telebot.types import Message

from keyboards.default import register_button
from keyboards.inline import translate_button

@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    db.insert_telegram_id(from_user_id)
    check = db.check_user(from_user_id)
    if None in check:
        text = "Assalomu alekum ro'yxatdan o'ting👇"
        markup = register_button()
    else:
        text = 'Tarjima qilish uchun tugmani ustiga bosing'
        markup = translate_button()
    bot.send_message(chat_id, text, reply_markup=markup)