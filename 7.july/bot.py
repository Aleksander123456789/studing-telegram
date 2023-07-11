from aiogram import Bot, Dispatcher, executor, types

#токен вашего бота
TOKEN = ''

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Словарь для хранения анонимных чатов
anonymous_chats = {}

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("Добро пожаловать в анонимный чат! Отправьте команду /join, чтобы присоединиться к анонимному чату.")

@dp.message_handler(commands=['join'])
async def join_handler(message: types.Message):
    chat_id = message.chat.id
    anonymous_chats[chat_id] = set()
    await message.answer("Вы присоединились к анонимному чату. Все ваши сообщения будут анонимными.")

@dp.message_handler()
async def anonymous_chat(message: types.Message):
    chat_id = message.chat.id
    if chat_id in anonymous_chats:
        # Отправляем сообщение анонимно всем участникам чата, кроме отправителя
        for participant_id in anonymous_chats[chat_id]:
            if participant_id != chat_id:
                await bot.send_message(participant_id, message.text)
    else:
        await message.answer("Присоединитесь к анонимному чату, отправив команду /join.")

@dp.message_handler(commands=['leave'])
async def leave_handler(message: types.Message):
    chat_id = message.chat.id
    if chat_id in anonymous_chats:
        del anonymous_chats[chat_id]
        await message.answer("Вы покинули анонимный чат.")
    else:
        await message.answer("Вы не присоединены к анонимному чату.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)