from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def generate_translator():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons_1 = KeyboardButton(text='🇷🇺-🇬🇧')
    buttons_2 = KeyboardButton(text='🇬🇧-🇷🇺')
    markup.row(buttons_1, buttons_2)
    return markup
