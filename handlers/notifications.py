import aioschedule
from aiogram import types,Dispatcher
from config import bot
import asyncio



async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer("OK!")

async def weather():
    url = 'https://www.gismeteo.ru/weather-yuzhno-kurilsk-4896/'
    await bot.send_message(chat_id=chat_id, text=f'Время проверить погоду\n{url}')


async def scheduler():
    aioschedule.every().tuesday.at("13:47").do(weather)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notifications(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: "Погода" in word.text)