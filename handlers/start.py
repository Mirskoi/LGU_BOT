from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards.reply import main

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        'Приветствую, я бот студ.совета ЛГУ. Выбери пункт меню:',
        reply_markup=main
    )