import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.types import Message
from aiogram.filters import Command

# Загружаем переменные окружения из .env
load_dotenv()
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не установлен. Проверь .env файл или переменные окружения.")

# Создаём бота с новыми настройками по версии aiogram 3.7+
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode="HTML")
)

dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Я твой первый бот на aiogram 🚀")

# Точка входа
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())