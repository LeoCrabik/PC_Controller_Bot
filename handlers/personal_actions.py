from aiogram import types
from aiogram.types import ContentTypes
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import os
from dispatcher import dp
import keyboards as kb

@dp.message_handler(commands=["start"])
async def setlink_command(message: types.Message):
	await message.answer("Здравствуйте, " + message.from_user.first_name + ". Выберете, что вы хотите сделать с компьютером", reply_markup=kb.startkb)

