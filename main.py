import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from config.config import TOKEN
from handlers import start, week, canteen, admin, anonym, schedule
from utils.db import init_db

async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())
    init_db()
    dp.include_routers(
        anonym.router,
        start.router,
        week.router,
        canteen.router,
        admin.router,
        schedule.router
    )
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        print('Бот запущен.')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')