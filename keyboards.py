from telebot import types
from bot_callbacks import Callbacks

class Keyboards:
    @classmethod
    def start_keyboard(cls):
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        item_btn_1 = types.KeyboardButton('Женщине')
        item_btn_2 = types.KeyboardButton('Мужчине')
        markup.add(item_btn_1, item_btn_2)
        return markup

    @classmethod
    def more_man_keyboard(cls):
        inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
        item_btn_1 = types.InlineKeyboardButton('Далее', callback_data=Callbacks.MORE_MAN)
        item_btn_2 = types.InlineKeyboardButton('Назад', callback_data=Callbacks.BACK)
        inline_keyboard.row(item_btn_1, item_btn_2)
        return inline_keyboard

    @classmethod
    def more_woman_keyboard(cls):
        inline_keyboard = types.InlineKeyboardMarkup(row_width=2)
        item_btn_1 = types.InlineKeyboardButton('Далее', callback_data=Callbacks.MORE_WOMAN)
        item_btn_2 = types.InlineKeyboardButton('Назад', callback_data=Callbacks.BACK)
        inline_keyboard.row(item_btn_1, item_btn_2)
        return inline_keyboard
