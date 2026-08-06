import os
from dotenv import load_dotenv

load_dotenv()

REQUIRED_DB_VARS = ("DB_HOST", "DB_PORT", "DB_NAME", "DB_USER", "DB_PASS")

variables = {name: os.getenv(name) for name in REQUIRED_DB_VARS}

missing = [name for name in REQUIRED_DB_VARS if not variables[name]]
if missing:
    raise RuntimeError(
        f"Missing required environment variable(s): {', '.join(missing)}. "
        "Copy .env.example to .env and fill in the database settings."
    )

database_connection = (
    f"postgresql://{variables['DB_USER']}:{variables['DB_PASS']}"
    f"@{variables['DB_HOST']}:{variables['DB_PORT']}/{variables['DB_NAME']}"
)
