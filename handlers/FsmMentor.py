from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import random
from config import bot
from Keyboards.client_kb import submit_markup, cancel_markup, direction_markup


class FSMMentor(StatesGroup):
    ID = State()
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()

async def fsm_start(message: types.Message):
    if message.from_user.first_name == '°-°':
        if message.chat.type == 'private':
            await FSMMentor.ID.set()
            await message.answer(f'hello! {message.from_user.full_name}\n'
                                         f'I will give you your ID', reply_markup=cancel_markup)
        else:
            await message.answer('Go to private chat!')
    else:
        await message.answer("YOU AREN'T MY BOSS!\n HEH LOSER")


async def mentor_ID(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['ID'] = random.randint(1,1000000)
        # print(data)
    await FSMMentor.next()
    await message.answer('What is your name?')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMMentor.next()
    await message.answer('What is your direction?', reply_markup=direction_markup)


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMMentor.next()
    await message.answer('What is your age?')


async def load_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await FSMMentor.next()
    await message.answer('What is your group?')

async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
        await message.answer(f"Id: {data['ID']}\nName: {data['name']}\nDirection: {data['direction']}\nAge {data['age']}\nGroup {data['group']}")
    await FSMMentor.next()
    await message.answer('Everything right?', reply_markup=submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'yes':
        await state.finish()
        await message.answer('Registration is over!')
    if message.text.lower() == 'no':
        await state.finish()
        await message.answer('Cancel')


async def cancel_reg(message: types.Message, state: FSMContext):
    curren_state = await state.get_state()
    if curren_state is not None:
        await state.finish()
        await message.answer('Well, okaay -_-')




def register_handlers_fsm_list_of_mentors(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True), state='*')

    dp.register_message_handler(fsm_start, commands=['list'])
    dp.register_message_handler(mentor_ID, state=FSMMentor.ID)
    dp.register_message_handler(load_name, state=FSMMentor.name)
    dp.register_message_handler(load_direction, state=FSMMentor.direction)
    dp.register_message_handler(load_age, state=FSMMentor.age)
    dp.register_message_handler(load_group, state=FSMMentor.group)
    dp.register_message_handler(submit, state=FSMMentor.submit)
