import os

import telebot
from dotenv import load_dotenv
from database.database import initialize_database

load_dotenv()
api_token = os.getenv('API_TOKEN')

if not api_token:
    raise ValueError("API Token is missing! Please check your .env file.")

bot = telebot.TeleBot(api_token)

from handlers.bot_handlers import *
initialize_database()


if __name__ == "__main__":

    print("Bot is starting...")
    bot.polling(none_stop=True)
