from flask import Flask
from threading import Thread
import importlib
from pyrogram import Client, idle
from INSTA import app, LOGGER
from INSTA.Module import ALL_MODULES
bot = Flask(__name__)
def load_modules():
    for all_module in ALL_MODULES:
        importlib.import_module("Sanatan.Module." + all_module)
    LOGGER.info("All modules loaded successfully.")
@bot.route('/')
def home():
    return "Bot is running!"
def start_bot():
    app.start()  
    LOGGER.info("Pyrogram bot started successfully.")
    idle() 
    app.stop() 
    LOGGER.info("Pyrogram bot stopped.")
def start_flask():
    LOGGER.info("Starting Flask server...")
    bot.run(host='0.0.0.0', port=5000)
if __name__ == "__main__":
    load_modules() 
    flask_thread = Thread(target=start_flask, daemon=True)
    flask_thread.start()
    start_bot()
