from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_panel = InlineKeyboardMarkup(inline_keyboard=
[
    [InlineKeyboardButton(text='Обновить меню', callback_data='admin_menu_update')]
])