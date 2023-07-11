







dp = Dispatcher(bot, storage=MemoryStorage())

active_users: set[int] = set
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    active_users.add(message.from_user.id)
    await message.answer("Добро пожаловать в комнату!")
    
@dp.message_handler()