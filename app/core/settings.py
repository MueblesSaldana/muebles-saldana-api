from pydantic import AnyHttpUrl, BaseSettings, EmailStr, validator
from typing import List, Optional, Union
import os


class Settings(BaseSettings):
    API_V1                      : str = "/v1"
    MONGO_URI                   : str

    JWT_SECRET                  : str
    ALGORITHM                   : str
    KEY                         : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int
    class Config:
        case_sensitive = True
        env_file = os.path.abspath("app/.env")  # Importo los valores del .env


settings = Settings()
