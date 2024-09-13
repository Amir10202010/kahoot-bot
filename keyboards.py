from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,  InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start = ReplyKeyboardMarkup(keyboard = [
    [KeyboardButton(text = 'Играть')],
    [KeyboardButton(text = 'О Игре'), KeyboardButton(text = 'Настройки')]
], one_time_keyboard = True, input_field_placeholder = 'Выберите пункт меню')

back = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Назад', callback_data = 'back')]
])

settings = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = '-5', callback_data = '-'),
     InlineKeyboardButton(text = '+5', callback_data = '+')],
    [InlineKeyboardButton(text = 'Назад', callback_data = 'back')]
])

end = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = 'Закончить тест', callback_data = 'end'),
    InlineKeyboardButton(text = 'Начать сначала', callback_data = 'again')]
])

def test(row):
    keyboard = ReplyKeyboardBuilder()
    for i in range(1, 5):
        keyboard.add(KeyboardButton(text = str(row[i])))
    return keyboard.adjust(2).as_markup(one_time_keyboard = True, input_field_placeholder = 'Ответьте на вопрос')