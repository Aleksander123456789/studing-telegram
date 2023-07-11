from __future__ import annotations

from config import TOKEN

from aiogram import Bot, Dispatcher, executor, types

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.types import message

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from keyboards import

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.messagr_handler(commands=['start'], state='*')
async def start_handler(message: Message, state: FSMContext):
    await message.answer
    
    
    
async def name_handler(message: Message, state: FSMContext):
    