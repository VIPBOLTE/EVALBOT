import re
import sys
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    @staticmethod
    def _get_env_var(var_name: str, default=None, is_int=False):
        value = getenv(var_name, default)
        if value is None:
            print(f"ERROR: Environment variable '{var_name}' is not set and no default was provided.")
            sys.exit(1)

        if is_int:
            try:
                return int(value)
            except ValueError:
                print(f"ERROR: Environment variable '{var_name}' should be an integer.")
                sys.exit(1)
        return value

    # Required Bot Configurations
    API_ID = _get_env_var.__func__("API_ID", None, is_int=True)
    API_HASH = _get_env_var.__func__("API_HASH", None)
    BOT_TOKEN = _get_env_var.__func__("BOT_TOKEN", None)
    OWNER_USERNAME = _get_env_var.__func__("OWNER_USERNAME", "Deletedaccounto11")
    BOT_USERNAME = _get_env_var.__func__("BOT_USERNAME", "Seal_Your_Waifu_Bot")
    MONGO_DB_URI = _get_env_var.__func__("MONGO_DB_URI", None)
    LOGGER_ID = _get_env_var.__func__("LOGGER_ID", None, is_int=True)
    OWNER_ID = _get_env_var.__func__("OWNER_ID", None, is_int=True)

    # Optional / Heroku-related
    HEROKU_APP_NAME = _get_env_var.__func__("HEROKU_APP_NAME", None)
    HEROKU_API_KEY = _get_env_var.__func__("HEROKU_API_KEY", None)

    # Git Upstream
    UPSTREAM_REPO = _get_env_var.__func__("UPSTREAM_REPO", "https://github.com/VIPBOLTE/EVALBOT")
    UPSTREAM_BRANCH = _get_env_var.__func__("UPSTREAM_BRANCH", "main")
    GIT_TOKEN = _get_env_var.__func__("GIT_TOKEN", None)

    # Support
    SUPPORT_CHANNEL = _get_env_var.__func__("SUPPORT_CHANNEL", "channelz_k")
    SUPPORT_CHAT = _get_env_var.__func__("SUPPORT_CHAT", "LOVING_SOCIETY")
