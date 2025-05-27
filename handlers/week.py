from datetime import datetime

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(F.text == "Какая неделя")
async def what_week(message: Message):
    now = datetime.now()
    week_num = now.isocalendar().week
    await message.answer(f"Сейчас {'нижняя' if week_num%2==0 else 'верхняя'} неделя.")
