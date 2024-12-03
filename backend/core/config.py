import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str = "API Preços"
    PROJECT_VERSION: str = "1.0.0"

    # sqlite
    DATABASE_URL : str = os.getenv("SQLITE_URL")
    DB_NAME: str = "../preco.db"

    # token
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Geral
    TICKER_SYMBOL: str = "AAPL"

settings = Settings()
