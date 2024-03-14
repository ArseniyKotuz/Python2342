import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold

TOKEN="6481605447:AAEwiyOljJciqSo_zw-2LvfFxUJ3AhQMwhk"
print(TOKEN)

dp = Dispatcher()

@dp.message(CommandStart())
async def comman_stat_handler(message: Message):
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message()
async def echo_handler(message: Message):
    try: 
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply("Nice try")


async def main():
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())