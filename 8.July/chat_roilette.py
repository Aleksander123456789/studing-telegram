from __future__ import annotations


from aiogram import Bot, Dispatcher, executor, types

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
bot = Bot(TOKEN2)
dp = Dispatcher(bot, storage=MemoryStorage())

waiting_users: set[int] = set()
connected_pairs: dict[int, int] = {}

@dp.message_handler(commands =['start'], state='*')
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer('Привет! Добро пожаловать в чат рулетку! Как тебя зовут?')
    await state.set_state('name')
    
@dp.message_handler(state='name')
async def name_handler(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({'name' : name})
    await message.replay(f'Приятно {name}! Жми /find чтобы начать общаться')
    await state.set_state('ready')
    
    
    
    
    
    
@dp.message_handler(commands ='find', state='ready')
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer('Ищем собеседника...')
    waiting_users.add(message.from_user.id)
    print(message.from_user)
    while len(waiting_users) >= 2:
        user_1_id = waiting_users.pop()
        user_2_id = waiting_users.pop()
        
        await dp.current_state(chat = user_1_id, user = user_1_id).set_state('chatting')
        await dp.current_state(chat = user_2_id, user = user_1_id).set_state('chatting')
        
        connected_pairs[user_1_id] = user_2_id
        connected_pairs[user_2_id] = user_1_id
        
        await bot.send_message(chat_id=user_1_id, text='Вы начали общаться')
        await bot.send_message(chat_id=user_2_id, text='Вы начали общаться')

@dp.message_handler(state='chatting')
async def chatting_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    chatmate_id = connected_pairs[user_id]
    await bot.send_message(chat_id=chatmate_id, text=message.text)


@dp.message_handler()
async def error_handler(message: types.Message, state: FSMContext):
    await message.reply(f'Неверный формат сообщения. Ваш текущий state: {await state.get_state()}')
    
executor.start_polling(dp, skip_updates=True)