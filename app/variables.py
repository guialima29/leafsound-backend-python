import os
from dotenv import load_dotenv

load_dotenv()

variables = {
    "DB_HOST": os.getenv("DB_HOST"),
    "DB_PORT": os.getenv("DB_PORT"),
    "DB_NAME": os.getenv("DB_NAME"),
    "DB_USER": os.getenv("DB_USER"),
    "DB_PASS": os.getenv("DB_PASS"),
}

database_connection = f"postgresql://{variables['DB_USER']}:{variables['DB_PASS']}@{variables['DB_HOST']}:{variables['DB_PORT']}/{variables['DB_NAME']}"