import os
from dotenv import load_dotenv
from datetime import datetime

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

    # Parametros do Modelo LSTM
    DT_START_TRAIN:  str = '2024-06-01'
    DT_END_TRAIN: str = '2024-09-30'
    DT_START_VALID: str = '2024-10-01'
    DT_END_VALID: str = '2024-10-31'
    NUM_EXAMPLES: int = 1
    VAL_SIZE: int = 30

settings = Settings()
