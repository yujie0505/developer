import os

from dotenv import load_dotenv

load_dotenv(verbose=True)


def get_env(key: str) -> str | None:
    """Get environment variables after loading the .env file."""
    return os.getenv(key)
