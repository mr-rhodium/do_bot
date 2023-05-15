import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from aioredis.client import Redis
from app.echo import router as echo_router
from settings import API_TOKEN, REDIS
from app.periodic import cron
logger = logging.getLogger(__name__)

async def on_startup(bot: Bot):
    pass

# import aiocron
# @aiocron.crontab('*/1 * * * *')
# async def time():
#     print("I am time ")
async def main():


    redis_client = Redis.from_url(REDIS.SERVER_PORT)
    
    storage=RedisStorage(redis=redis_client)
    bot: Bot = Bot(token=API_TOKEN,  parse_mode="HTML")
    storage: MemoryStorage = MemoryStorage()
    dp: Dispatcher = Dispatcher(storage=storage)
    await cron(redis_client)

    dp.include_router(echo_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        logger.info("Start")
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Stopped")

    
# import logging
# from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.fsm_storage.memory import MemoryStorage

# # Установка уровня логирования
# logging.basicConfig(level=logging.INFO)

# # Инициализация бота и диспетчера
# bot = Bot(token="YOUR_TOKEN")
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)

# # Обработчик команды /start
# @dp.message_handler(commands=['start'])
# async def start_handler(message: types.Message):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     buttons = ["Button 1", "Button 2", "Button 3"]
#     keyboard.add(*buttons)
#     await message.reply("Привет! Выбери одну из кнопок:", reply_markup=keyboard)

# # Обработчик кнопок
# @dp.message_handler(content_types=types.ContentTypes.TEXT)
# async def button_handler(message: types.Message):
#     if message.text == "Button 1":
#         await message.reply("Вы выбрали кнопку 1")
#     elif message.text == "Button 2":
#         await message.reply("Вы выбрали кнопку 2")
#     elif message.text == "Button 3":
#         await message.reply("Вы выбрали кнопку 3")

# # Запуск бота
# if __name__ == '__main__':
#     from aiogram import executor
#     executor.start_polling(dp, skip_updates=True)
