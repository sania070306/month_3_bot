from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp, ADMINS
import re
import random


# @dp.message_handler()
async def echo(message: types.Message):
    username = f'@{message.from_user.username}' \
        if message.from_user.username is not None else message.from_user.full_name
    if re.match(r"\d", message.text):
        number = int(message.text)
        await bot.send_message(message.from_user.id, number**2)
    else:
        bad_words = ['спорт','какашка', 'дурак', 'математика', 'физика', 'химия', 'школа' 'универ', 'пары']
        for word in bad_words:
            if word in message.text.lower():
                await bot.delete_message(message.chat.id, message.message_id)
                if word == bad_words[1] or word == bad_words[2]:
                    await message.answer(
                        f'Фу фу фу, как некультурно @{username}\n'
                        f'Сам ты {word}'
                    )
                else:
                    await message.answer(
                        f'Фу фу фу, как некультурно @{username}\n'
                        f'Врагу такое не пожелаешь '
                    )
            # else:
            #     await bot.send_message(message.from_user.id, message.text)

    if message.text.startswith('game'):
        if not message.from_user.id in ADMINS:
            await message.reply("Ты не мой босс!")
        else:
            list_of_emogi = ['⚽', '🏀', '🎳', '🎯', '🎲', '🎰']
            await bot.send_dice(message.chat.id, emoji=random.choice(list_of_emogi))



def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
