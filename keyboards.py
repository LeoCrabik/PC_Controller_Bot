from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

control_buttons = [
	types.InlineKeyboardButton(text="Выключить", callback_data = "PC_OFF"),
	types.InlineKeyboardButton(text="Перезагрузить", callback_data = "PC_REBOOT"),
    types.InlineKeyboardButton(text="Предупреждение", callback_data = "PC_WARNING")
]
startkb = types.InlineKeyboardMarkup(row_width=1, one_time_keyboard = True)
startkb.add(*control_buttons)

btn_start = KeyboardButton('/start')
start = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
start.add(btn_start)