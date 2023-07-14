from __future__ import annotations

import os
from typing import Callable

from dotenv import load_dotenv


def load(dotenv_path: str | None = None) -> Callable[[str], str | None]:
    """Load environment variables from dotenv file."""
    load_dotenv(dotenv_path, verbose=True)

    return lambda key: os.getenv(key)
