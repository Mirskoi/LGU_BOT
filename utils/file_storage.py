import os
from config.config import PHOTO_STORAGE_PATH

def save_photo(file_id: str, file_path: str):
    os.makedirs(PHOTO_STORAGE_PATH, exist_ok=True)
    full_path = os.path.join(PHOTO_STORAGE_PATH, f"{file_id}.jpg")
    return full_path
