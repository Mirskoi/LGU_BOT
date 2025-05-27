from dotenv import load_dotenv
import os
from utils.db import admins_get

load_dotenv()
TOKEN = os.getenv("BOT_API_TOKEN")
ADMIN_IDS = admins_get()
ADMIN_CHAT = -1002400437092
PHOTO_STORAGE_PATH='data/photos'