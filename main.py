import telebot
from keybords import generate_translator
from perevod import bot_translate

API_TOKEN = 'TOKEN'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Ты запустил телеграм бота переводчик')
    bot.send_message(message.chat.id, 'Выбери перевод', reply_markup=generate_translator())


@bot.message_handler()
def handle_messages_with_emojis(message):
    if message.text == '🇷🇺-🇬🇧':
        _ = bot.send_message(message.chat.id, 'Введите слово которое хотите перевести: ')
        bot.register_next_step_handler(_,  message_text, 'ru', 'en',)
    elif message.text == '🇬🇧-🇷🇺':
        _ = bot.send_message(message.chat.id, 'Введите слово которое хотите перевести: ')
        bot.register_next_step_handler(_,  message_text, 'en', 'ru',)
    else:
        bot.reply_to(message, 'Извините я не понял вас')


def message_text(message, from_l, to_l):
    messageText = message.text
    finish_message = bot_translate(from_l, to_l, str(messageText))
    bot.send_message(message.chat.id, finish_message)


bot.infinity_polling()
