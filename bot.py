import os
import openai
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
openai.api_key = OPENAI_API_KEY

@dp.message_handler()
async def chat_with_gpt(message: types.Message):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": message.text}]
    )
    await message.reply(response["choices"][0]["message"]["content"])

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
