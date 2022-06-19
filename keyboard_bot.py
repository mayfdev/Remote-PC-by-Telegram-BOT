from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

space_b = KeyboardButton('🔽 Пробел')
right_b = KeyboardButton('⏩ Перемотать в перед')
left_b = KeyboardButton('⏪  Перемотать назад')
sleap_b = KeyboardButton('💤 Уйти в сон')
remote = ReplyKeyboardMarkup(resize_keyboard=True)

remote.add(space_b, right_b, left_b, sleap_b)