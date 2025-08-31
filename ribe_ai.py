import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram import F
from aiogram.filters import Command

TOKEN = "7579930042:AAG3SBzgC-RTcGvDzf3uPCri-VU5eitbPUU"

load_dotenv() 
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не установлен. Проверь .env файл или переменные окружения.")
bot = Bot(token=TOKEN)
dp = Dispatcher()

# простой обработчик команды /start
@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Привет! Я твой первый бот на aiogram 🚀")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())