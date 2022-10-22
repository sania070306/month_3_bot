from aiogram import types, Dispatcher
from config import bot, dp
from database.bot_db import sql_command_delete
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# @dp.callback_query_handler(lambda call: call.data == 'button_call')
async def quiz_2(call: types.CallbackQuery ):
    question = 'Почему плутон лишили статуса планеты?'
    answers = [
        'Слишком маленькая',
        'Далековато',
        'Учёным не нравится эта планета',
        'Плутон не способен очистить свою орбиту от небесных тел',
        'Ну так вышло ;-;'
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3
    )



def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == 'button_call')

