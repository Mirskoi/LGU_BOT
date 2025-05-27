from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from datetime import datetime
from utils.db import admin_add
from config.config import ADMIN_IDS
from utils.db import save_canteen_menu
from utils.file_storage import save_photo
from keyboards.inline import admin_panel

router = Router()

class AdminMenuForm(StatesGroup):
    menu = State()

@router.callback_query(F.data == 'admin_menu_update')
async def start_update_menu(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('Отправьте новую фотографию меню.')
    await state.set_state(AdminMenuForm.menu)
    await callback.answer()

@router.message(AdminMenuForm.menu, F.photo)
async def update_menu(message: Message, state: FSMContext, bot):
    date = datetime.now().strftime("%Y-%m-%d")
    photo = message.photo[-1]
    file_id = photo.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    local_path = save_photo(file_id, file_path)
    try:
        await bot.download_file(file_path, local_path)
    except Exception as e:
        print(f"Ошибка сохранении фото: {e}")
        await message.answer("Ошибка при сохранении фото. Попробуйте снова.")
        await state.clear()
        return
    save_canteen_menu(date, local_path)
    await message.answer(f"Расписание на {date} сохранено!")
    await state.clear()

@router.message(Command('admin'))
async def cmd_admin(message: Message):
    if message.from_user.id not in ADMIN_IDS:
        await message.reply('Вы не админ, кыш отсюда.')
        return
    await message.answer(f'<b>Крутая админ панель, для крутых админов:</b>', reply_markup=admin_panel)

# @router.message(Command('add_admin'))
# async def cmd_admin(message: Message):
#     if message.from_user.id is not 1730684404:
#         await message.reply('Вы не бог, кыш отсюда.')
#         return
    
    
    