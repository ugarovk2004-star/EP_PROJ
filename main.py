# main.py
import asyncio
import logging
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from middlewares.input_validation import InputValidationMiddleware

# Импорт роутеров
from handlers.common import router as common_router
from handlers.copycenter import router as copycenter_router
from handlers.polygraphy import router as polygraphy_router
from handlers.packaging import router as packaging_router
from handlers.interior import router as interior_router
from handlers.souvenirs import router as souvenirs_router
from handlers.stamps import router as stamps_router
from handlers.photoprint import router as photoprint_router
from handlers.order_confirmation import router as order_confirmation_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # Регистрируем middleware
    dp.update.outer_middleware(InputValidationMiddleware())

    
    # Регистрация всех роутеров
    dp.include_router(common_router)
    dp.include_router(copycenter_router)
    dp.include_router(polygraphy_router)
    dp.include_router(packaging_router)
    dp.include_router(interior_router)
    dp.include_router(souvenirs_router)
    dp.include_router(stamps_router)
    dp.include_router(photoprint_router)
    dp.include_router(order_confirmation_router)
    
    # Запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())