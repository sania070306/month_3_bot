from aiogram import types, Dispatcher
from config import bot, dp
from database.bot_db import sql_command_all, sql_command_delete
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def delete_data(message: types.Message):
    users = await sql_command_all()
    for user in users:
        await bot.send_message(message.from_user.id, f'ID: {user[0]}\n'
                                                 f'Name: {user[1]}\nDirection: {user[2]}\n'
                                                 f'Age: {user[3]}\nGroup: {user[4]}\n',
                               reply_markup=InlineKeyboardMarkup().add(
                                   InlineKeyboardButton(f"delete {user[1]}", callback_data=f'delete {user[0]}')
                               ))

async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace('delete ', ''))
    await call.answer(text='go out!', show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(delete_data, commands=['del'])
    dp.callback_query_handler(complete_delete, lambda call: call.data and call.data.startwith("delete "))

