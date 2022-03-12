from click import command
import keyboard
import os

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

space_b = KeyboardButton('🔽 Пробел')
right_b = KeyboardButton('⏩ Перемотать в перед')
left_b = KeyboardButton('⏪  Перемотать назад')
sleap_b = KeyboardButton('💤 Уйти в сон')
remote = ReplyKeyboardMarkup(resize_keyboard=True)
remote.add(space_b, right_b, left_b, sleap_b)



@dp.message_handler(commands=['start'])
async def START(message: types.Message):
    await message.answer('<code>🎆 Добро Пожаловать</code>\n<i>by <a href="https://lolz.guru/threads/3526061">MAYFDEV</a></i>', parse_mode= types.ParseMode.HTML, reply_markup=remote)

async def SPACE(message: types.Message):
    keyboard.press_and_release('space')
    await message.answer('🔽')

async def RIGHT(message: types.Message):
    keyboard.press_and_release('right')
    await message.answer('⏩')

async def LEFT(message: types.Message):
    keyboard.press_and_release('left') 
    await message.answer('⏪')

async def SLEAP(message: types.Message):
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0") 
    await message.answer('💤')

@dp.message_handler(content_types=['text'])
async def main(message : types.Message):
    if message.text == '🔽 Пробел':
        await SPACE(message)
    if message.text == '⏩ Перемотать в перед':
        await RIGHT(message)
    if message.text == '⏪  Перемотать назад':
        await LEFT(message)
    if message.text == '💤 Уйти в сон':
        await SLEAP(message)
    
    

if __name__ == '__main__':
    executor.start_polling(dp)