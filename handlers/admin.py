from aiogram import types, Dispatcher
from config import bot, dp, ADMINS
from database.bot_db import sql_command_all
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random


async def delete_data(message: types.Message):
    users = await sql_command_all()
    for user in users:
        await bot.send_message(message.from_user.id, f'ID: {user[0]}\n'
                                                 f'Name: {user[1]}\nDirection: {user[2]}\n'
                                                 f'Age: {user[3]}\nGroup: {user[4]}\n',
                               reply_markup=InlineKeyboardMarkup().add(
                                   InlineKeyboardButton(f"delete {user[1]}", callback_data=f'delete {user[0]}')
                               ))

async def pin(message: types.Message):
    if message.chat.type == 'supergroup':
        if not message.from_user.id in ADMINS:
            await message.reply("Ты не мой босс!")
        elif not message.reply_to_message:
            await message.reply("какое сообщение закрепить?")
        else:
            await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
            await message.answer(
                f"закрепила"
            )
    else:
        await message.answer('пиши в группу!')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')


