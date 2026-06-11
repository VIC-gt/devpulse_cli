import json
import os
# Import the top-level User model to properly structure the database loader
from models.user import User

# Define the file system path where data will be read and written
STORAGE_FILE = "data/storage.json"

def load_data():
    # Defensive check: if the text file does not exist yet, return an empty array list safely
    if not os.path.exists(STORAGE_FILE):
        return []
    try:
        # Open the storage JSON text file in read mode
        with open(STORAGE_FILE, "r") as file_handle:
            raw_data = json.load(file_handle)
            # Rehydrate the plain JSON maps back into clean Python User Objects
            return [User.from_dict(user_data) for user_data in raw_data]
    except (json.JSONDecodeError, KeyError):
        # Gracefully handle file corruptions or empty string errors without crashing the CLI
        print("[Warning] System database file was corrupted. Initializing a clean session.")
        return []

def save_data(users_list):
    # Automatically build the data folder if it doesn't exist on the host computer path
    os.makedirs(os.path.dirname(STORAGE_FILE), exist_ok=True)
    # Open the text destination file in write mode to save data structures
    with open(STORAGE_FILE, "w") as file_handle:
        # Convert Python class instances to dictionary trees and export with human-readable spacing
        json.dump([user.to_dict() for user in users_list], file_handle, indent=4)