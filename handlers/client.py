from  aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from config import bot, dp
import random
from database.bot_db import sql_command_random
from parser.doramy import parser


# @dp.message_handler(commands=['start', 'info'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, f"Салалекум {message.from_user.first_name}!")

# @dp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo1 = open('media/img.png', 'rb')
    photo2 = open('media/img_1.png', 'rb')
    photo3 = open('media/img_2.png', 'rb')
    photo4 = open('media/img_3.png', 'rb')
    list_photo = [photo1, photo2, photo3, photo4]
    await bot.send_photo(message.from_user.id, photo=random.choice(list_photo))


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('NEXT', callback_data='button_call_1')
    markup.add(button_call_1)

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

async def get_random_user(message: types.Message):
    await sql_command_random(message)


async def parser_doramy(message: types.Message):
    items = parser()
    for item in items:
        await message.answer(
            f"{item['link']}\n\n"
            f"{item['title']}\n"
            f"#{item['series']}"
            f"#{item['country']}"
            f"#{item['year']}"
            f"#{item['genre']}"
            f"{item['status']}"
        )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start', 'info'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(get_random_user, commands=['get'])
    dp.register_message_handler(parser_doramy, commands=['kdramas'])
