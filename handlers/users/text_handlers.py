from data.loader import bot, db
from telebot.types import Message, ReplyKeyboardRemove

from handlers.users.name_checker import name_checker
from keyboards.default import phone_button
from keyboards.inline import translate_button
user_data = {}

@bot.message_handler(func=lambda message: message.text == "Ro'yxatdan o'tish")
def register(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    user_data[from_user_id] = {}
    msg = bot.send_message(chat_id, "Ismingizni kiriting", reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, get_name)

def get_name(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    fullname = message.text.split(' ')
    print(fullname)
    if name_checker(fullname):
        full_name = message.text
    else:
        msg = bot.send_message(chat_id, "Ismingizni bosh harfini katta bilan lotin harflarida kiriting")
        bot.register_next_step_handler(msg, get_name)

    user_data[from_user_id]['full_name'] = full_name
    msg = bot.send_message(chat_id, "Telefon raqamni yuborish uchun tugmani bosing", reply_markup=phone_button())
    bot.register_next_step_handler(msg, save_user)

def save_user(message: Message):
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    full_name = user_data[from_user_id]['full_name']
    phone_number = None
    if message.contact:
        phone_number = message.contact.phone_number
    elif message.text.startswith('+998') and len(message.text) == 13 and message.text[1:].isdigit():
        phone_number = message.text
    else:
        msg = bot.send_message(chat_id, "Telefon raqam noto'g'ri kiritildi boshqatdan urining", reply_markup=phone_button())
        bot.register_next_step_handler(msg, save_user)
    if phone_number:
        db.update_user(full_name, phone_number, telegram_id=from_user_id)
        del user_data[from_user_id]['full_name']
        bot.send_message(chat_id, "Ro'yxatdan o'tdingiz", reply_markup=ReplyKeyboardRemove())
        bot.send_message(chat_id, 'Tarjima qilish uchun tugmani ustiga bosing', reply_markup=translate_button())









