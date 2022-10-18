from aiogram import types, Dispatcher
# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
import re


# @dp.message_handler()
async def echo(message: types.Message):
    if re.match(r"\d", message.text):
        number = int(message.text)
        await bot.send_message(message.from_user.id, number**2)
    else:
        await bot.send_message(message.from_user.id, message.text)

def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
