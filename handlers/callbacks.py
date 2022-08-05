from os import write
import ctypes
from aiogram import types
from dispatcher import dp
from dispatcher import bot
import config
import keyboards as kb
from handlers import personal_actions as pa
import os
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



@dp.callback_query_handler(lambda call: call.data == "PC_REBOOT")
async def change_to_en_lang(callback: types.CallbackQuery):
	await callback.message.delete()
	await callback.message.answer("Компьютер успешно перезагружен", reply_markup=kb.start)
	os.system("shutdown /r /t  1")

@dp.callback_query_handler(lambda call: call.data == "PC_OFF")
async def change_to_en_lang(callback: types.CallbackQuery):
	await callback.message.delete()
	await callback.message.answer("Компьютер успешно выключен", reply_markup=kb.start)
	os.system('shutdown /p /f')

@dp.callback_query_handler(lambda call: call.data == "PC_WARNING")
async def change_to_en_lang(callback: types.CallbackQuery):
	await callback.message.delete()
	await callback.message.answer("Предупреждение успешно отправлено", reply_markup=kb.start)
	ctypes.windll.user32.MessageBoxW(0, u"Предупреждение", u"Заебал орать", 0) 

	