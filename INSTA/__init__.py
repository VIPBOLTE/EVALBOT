import logging
from pyrogram import Client
from motor.motor_asyncio import AsyncIOMotorClient
from config import Config

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

# Initialize Pyrogram client and MongoDB client
app = Client("INSTA", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)
lol = AsyncIOMotorClient(Config.MONGO_DB_URI)

# MongoDB collections
db = lol['SEAL_CHARACTER']
pm_users = db['total_pm_users']
bot_working = db['bot_working']
sent_photos = db['sent_photos']
images_collection = db["images"]
