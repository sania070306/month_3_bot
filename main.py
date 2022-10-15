from aiogram import types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
import random
import logging
import re

@dp.message_handler(commands=['start', 'info'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, f"Салалекум {message.from_user.first_name}!")

@dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo1 = open('media/img.png', 'rb')
    photo2 = open('media/img_1.png', 'rb')
    photo3 = open('media/img_2.png', 'rb')
    photo4 = open('media/img_3.png', 'rb')
    list_photo = [photo1, photo2, photo3, photo4]
    await bot.send_photo(message.from_user.id, photo=random.choice(list_photo))


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call = InlineKeyboardButton('NEXT', callback_data='button_call')
    markup.add(button_call)
    question = 'Какой формы земля?'
    answers = [
        'Круглой формы',
        'Формы картошки',
        'Эллипсоидной формы',
        'Земля плоская',
        'Форма куба'
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        reply_markup=markup
    )

@dp.callback_query_handler(lambda call: call.data == 'button_call')
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



@dp.message_handler()
async def echo(message: types.Message):
    if re.match(r"\d", message.text):
        number = int(message.text)
        await bot.send_message(message.from_user.id, number**2)
    else:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
