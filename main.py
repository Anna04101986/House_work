# import logging
import time
import flask
from get_about import GetAbout
import telebot
import urls
from telebot.types import Message, CallbackQuery
from keyboards import Keyboards
from bot_callbacks import Callbacks
from config import *




# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)
bot = telebot.TeleBot(API_TOKEN)
getAbout = GetAbout()
app = flask.Flask(__name__)
time.sleep(0.1)



@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    bot.send_message(message.chat.id,
                 "Привет, я бот. Я умею поздравлять с днем рождения", reply_markup=Keyboards.start_keyboard())

@bot.callback_query_handler(func=lambda call: True)
def handle(call: CallbackQuery):
    if call.data == Callbacks.MORE_MAN:
        congratulation, amount = getAbout.get_man(urls.man)
        bot.send_message(call.message.chat.id, f'{congratulation}\n{amount}', reply_markup=Keyboards.more_man_keyboard())

    elif call.data == Callbacks.MORE_WOMAN:
        congratulation, amount = getAbout.get_woman(urls.woman)
        bot.send_message(call.message.chat.id, f'{congratulation}\n{amount}', reply_markup=Keyboards.more_woman_keyboard())

    elif call.data == Callbacks.BACK:
        bot.send_message(call.message.chat.id, 'И снова здравствуйте', reply_markup=Keyboards.start_keyboard())



@bot.message_handler(func=lambda message: True, content_types=['text'])
def message(message: Message):
    if message.text == 'Мужчине':
        congratulation, amount = getAbout.get_man(urls.man)
        print(congratulation)
        bot.send_message(message.chat.id, f'{congratulation}\n{amount}', reply_markup=Keyboards.more_man_keyboard())
    elif message.text == 'Женщине':
        congratulation, amount = getAbout.get_woman(urls.woman)
        bot.send_message(message.chat.id, f'{congratulation}\n{amount}', reply_markup=Keyboards.more_woman_keyboard())


# Process webhook calls
@app.route('/' + API_TOKEN, methods=['POST', 'GET'])
def webhook():
    # logger.debug("gas")
    # logger.debug(flask.request.get_data())
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')

        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])

        return '200'
    else:
        flask.abort(403)


bot.remove_webhook()
# bot.infinity_polling()
bot.set_webhook(WEBHOOK_URL + "/" + API_TOKEN)
app.run(host=WEBHOOK_HOST,port=WEBHOOK_PORT)