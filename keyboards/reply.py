from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder='Выберите пункт.',
keyboard=[
    [KeyboardButton(text='Какая неделя'), KeyboardButton(text='Расписание звонков')],
    [KeyboardButton(text='Меню столовой'), KeyboardButton(text='Анонимное обращение')]
])