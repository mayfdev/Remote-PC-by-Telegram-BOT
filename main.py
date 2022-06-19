
import keyboard
import os
from keyboard_bot import *
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import pyautogui
from config import TOKEN
from clear_cache import clear as clear_cache



bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)



@dp.message_handler(commands=['start'])
async def START(message: types.Message):
    await bot.delete_message(message.chat.id, message.message_id)
    await message.answer('<code>🎆 Добро Пожаловать</code>\n\n<b>Бот создан для удаленного доступа к компютеру</b>\n\n<i>by <a href="https://lolz.guru/threads/3526061">MAYFDEV</a></i>', parse_mode= types.ParseMode.HTML, reply_markup=remote)

async def SPACE(message: types.Message):
    await bot.delete_message(message.chat.id, message.message_id)
    keyboard.press_and_release('space')
    await message.answer('🔽')

async def RIGHT(message: types.Message):
    await bot.delete_message(message.chat.id, message.message_id)
    keyboard.press_and_release('right')
    await message.answer('⏩')

async def LEFT(message: types.Message):
    await bot.delete_message(message.chat.id, message.message_id)
    keyboard.press_and_release('left') 
    await message.answer('⏪')

async def SLEAP(message: types.Message):
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    await bot.delete_message(message.chat.id, message.message_id)
    clear_cache(dir = ".")
    await message.answer('💤')
    raise SystemExit
    

async def SCREANSHOT(message: types.Message):
    screenshot_do = pyautogui.screenshot()
    screenshot_do.save("MayfDEV_screen.png")
    screenshot_file = open('MayfDEV_screen.png', 'rb')

    await bot.send_document(
        caption='Вот ваш скриншот :)',
        document=screenshot_file,
        chat_id=message.chat.id
    )
    os.remove('MayfDEV_screen.png')

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
        return
    if message.text == '🌄 Скриншот':
        await SCREANSHOT(message)


if __name__ == '__main__':
    executor.start_polling(dp)