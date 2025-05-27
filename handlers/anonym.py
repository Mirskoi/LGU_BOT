from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from utils.db import save_anonym_message
from config.config import ADMIN_CHAT

router = Router()

class AnonymousForm(StatesGroup):
    waiting_for_message = State()

@router.message(F.text == "Анонимное обращение")
async def start_anonymous(message: Message, state: FSMContext):
    await message.answer("Напиши свое сообщение, оно будет отправлено анонимно.")
    await state.set_state(AnonymousForm.waiting_for_message)

@router.message(AnonymousForm.waiting_for_message)
async def process_anonymous_message(message: Message, state: FSMContext, bot):
    if not message.text:
        await message.answer("Пожалуйста, отправь текстовое сообщение.")
        return
    save_anonym_message(message.text, message.from_user.id)
    formatted_time = message.date.strftime("%H:%M %d.%m.%Y")
    try:
        await bot.send_message(
            chat_id=ADMIN_CHAT,
            text=f"<b>Поступило новое анонимное сообщение:</b>\n{message.text}\n<b>Время отправки:</b> {formatted_time}"
        )
    except Exception as e:
        print(f"Ошибка отправки анонимного сообщения админам: {e}")
    await message.answer("Ваще аномнимное сообщение было отправлено!")
    await state.clear()