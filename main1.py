import telebot
from telebot import types

TOKEN = "5521224900:AAHytaq5LDdk9sWbbjFwxjm3ZD5rc07ZsKM"

bot = telebot.TeleBot(TOKEN)

markup = types.ReplyKeyboardMarkup(row_width=2)
item_btn_1 = types.KeyboardButton('Start')
item_btn_2 = types.KeyboardButton('Help')
item_btn_3 = types.KeyboardButton('About_author')
markup.add(item_btn_1, item_btn_2, item_btn_3)

inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
item_btn_1 = types.InlineKeyboardButton('Start', callback_data='/start')
item_btn_2 = types.InlineKeyboardButton('Help', callback_data='/help')
item_btn_3 = types.InlineKeyboardButton('About_author', callback_data='/about_author')
inline_keyboard.row(item_btn_1,item_btn_2)
inline_keyboard.row(item_btn_3)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,
                     """Привет! Я умею следующие действия: 
                     рассказывать о себе (команда /about_author),
                     выводить клавиатуру из 3 кнопок (команда /get_keyboard),
                     возвращать клавиатуру как сообщение (команда /get_keyboard_inline)""")

@bot.callback_query_handler(func=lambda call: True)
def handle(call):
    # bot.send_message(call.message.chat.id, 'Data: {}'.format(str(call.data)))
    if call.data == '/start':
        bot.send_message(call.message.chat.id, 'Привет!')
    elif call.data == '/about_author':
        bot.send_message(call.message.chat.id, 'Привет! Меня зовут Анна. Я автор этого канал.')
    elif call.data == '/help':
        bot.send_message(call.message.chat.id, 'Могу я чем-нибудь помочь?')
    bot.answer_callback_query(call.id)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "text", reply_markup=inline_keyboard)


@bot.message_handler(commands=['about_author'])
def send_about(message):
    bot.send_message(message.chat.id, 'Я Анна, создатель этого бота.')

@bot.message_handler(commands=['get_keyboard'])
def send_keyboard(message):
    bot.send_message(message.chat.id, "Кнопки", reply_markup=markup)

@bot.message_handler(commands=['get_keyboard_inline'])
def send_keyboard_inline(message):
    bot.send_message(message.chat.id, "Сообщение", reply_markup=inline_keyboard)

@bot.message_handler(content_types=['text'])
def answers(message):
    if message.text == 'Start':
        bot.send_message(message.chat.id, "Здравствуйте!")
    elif message.text == 'Help':
        bot.send_message(message.chat.id, "Чем вам помочь?")
    elif message.text == 'About_author':
        bot.send_message(message.chat.id, "Я - Анна, я - создатель)!")
    else:
        bot.send_message(message.chat.id, message.text)


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#  	bot.reply_to(message, message.text)

# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#  	bot.send_message(message.chat.id, message.text)

bot.infinity_polling()
input()
