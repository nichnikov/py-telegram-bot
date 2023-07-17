import telebot
from telebot import types

bot = telebot.TeleBot('5905049745:AAGJSK1_eJVYsMfhM_aCHZ7p9_1Zrn7hRhA')

@bot.message_handler(commands = ['start'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='Наш сайт', url='https://habr.com/ru/all/')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на сайт хабра", reply_markup = markup)
