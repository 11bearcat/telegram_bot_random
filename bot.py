import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    #key
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рандомное число?")
    item2 = types.KeyboardButton("Как дела?")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, text='Hello man', parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Рандомное число?':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == "Как дела?":
            bot.send_message(message.chat.id, "Отлично, как сам?")
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить')

#RUN
bot.polling(none_stop=True)