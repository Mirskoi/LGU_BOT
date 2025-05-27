from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from utils.db import get_canteen_menu

router = Router()

@router.message(F.text == "Меню столовой")
async def show_canteen_menu(message: Message):
    photo_path = get_canteen_menu()
    if photo_path:
        photo = FSInputFile(photo_path)
        await message.answer_photo(photo, caption="Меню столовой на сегодня")
    else:
        await message.answer("Меню на сегодня не задано.")