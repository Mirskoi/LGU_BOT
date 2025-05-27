from aiogram import Router, F
from aiogram.types import Message, FSInputFile
from utils.db import get_canteen_menu

router = Router()

@router.message(F.text == "Расписание звонков")
async def show_canteen_menu(message: Message):
    await message.answer(f"Расписание учебных занятий:\n1 пара 9:00 - 10:20\n2 пара 10:30 - 11:50\n3 пара 12:50 - 14:10\n4 пара 14:20 - 15:40\n5 пара 15:50 - 17:10\n6 пара 17:20 - 18:40\n7 пара 18:50 - 20:10")