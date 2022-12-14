from aiogram import types, Dispatcher
from config import bot, dp
from database.bot_db import sql_command_delete
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# @dp.callback_query_handler(lambda call: call.data == 'button_call')
async def quiz_2(call: types.CallbackQuery ):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)

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
        correct_option_id=3,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    question = 'Я не знаю что тут придумать, просто потыкайте по кнопочкам :)'
    answers = [
        'Буль буль',
        '^-^',
        '*U*',
        'AaaAaaAaaaAaaaAaAAaaAAaAAAaAa',
        '@_@'
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
    )

async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(call.data.replace('delete ', ''))
    await call.answer(text='Oops, you destroyed it!', show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == 'button_call_1')
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == 'button_call_2')
    dp.register_callback_query_handler(complete_delete, lambda call: call.data and call.data.startswith("delete "))

