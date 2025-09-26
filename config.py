import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters
import sys

load_dotenv()

# Function to validate environment variables
def check_env_var(var_name, default_value, is_int=False):
    value = getenv(var_name, default_value)
    if is_int:
        try:
            return int(value)
        except ValueError:
            print(f"ERROR: {var_name} should be an integer!")
            sys.exit(1)
    return value

API_ID = check_env_var("API_ID", "28477444", True)  # Ensure it's an integer
API_HASH = check_env_var("API_HASH", "7cd9caeb99fdf37a5cf12b180e4b1b0b")
BOT_TOKEN = check_env_var("BOT_TOKEN", "6902253047:AAGCMdIPTLp3kNi5n_pMfiWnBroP3Rh2xYY")
OWNER_USERNAME = check_env_var("OWNER_USERNAME", "Deletedaccounto11")
BOT_USERNAME = check_env_var("BOT_USERNAME", "Seal_Your_Waifu_Bot")
MONGO_DB_URI = check_env_var("MONGO_DB_URI", "mongodb+srv://riyu:riyu@cluster0.kduyo99.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOGGER_ID = check_env_var("LOGGER_ID", "-1002126989582", True)
OWNER_ID = check_env_var("OWNER_ID", "5595153270", True)

# Heroku-related variables
HEROKU_APP_NAME = check_env_var("HEROKU_APP_NAME", None)
HEROKU_API_KEY = check_env_var("HEROKU_API_KEY", None)

UPSTREAM_REPO = check_env_var("UPSTREAM_REPO", "https://github.com/VIPBOLTE/Sanatan-cheat-bot")
UPSTREAM_BRANCH = check_env_var("UPSTREAM_BRANCH", "main")
GIT_TOKEN = check_env_var("GIT_TOKEN", None)
SUPPORT_CHANNEL = check_env_var("SUPPORT_CHANNEL", "channelz_k")
SUPPORT_CHAT = check_env_var("SUPPORT_CHAT", "LOVING_SOCIETY")
