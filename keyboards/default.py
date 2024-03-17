from telebot.types import ReplyKeyboardMarkup, KeyboardButton



def register_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = KeyboardButton("Ro'yxatdan o'tish")
    markup.add(btn1)
    return markup
def phone_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = KeyboardButton("Telefon raqamni yuborish", request_contact=True)
    markup.add(btn1)
    return markup