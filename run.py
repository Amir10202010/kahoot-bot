import asyncio
from aiogram import Bot, Dispatcher

from background import keep_alive
from config import TOKEN
from app.handlers import router

bot = Bot(token = TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        print('Запуск Бота')
        keep_alive()
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Завершение Бота')
