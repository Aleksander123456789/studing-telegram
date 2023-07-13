import aiogram
from aiogram import Bot, Dispatcher, types
import emoji
from config import TOKEN
# Создаем экземпляр бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет! Я бот расшифрователя эмодзи. Просто отправь мне эмодзи, и я расскажу тебе, что оно означает.")

# Обработчик текстовых сообщений с эмодзи
@dp.message_handler(content_types=types.ContentType.TEXT)
async def decode_emoji(message: types.Message):
    text = message.text
    decoded_text = emoji.demojize(text)
    await message.reply(f"Расшифровка: {decoded_text}")

# Запускаем бота
if __name__ == '__main__':
    aiogram.executor.start_polling(dp)
