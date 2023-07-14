from pydantic import BaseSettings,Field
from functools import lru_cache
import os


if os.getenv("CQLENG_ALLOW_SCHEMA_MANAGEMENT=0") is None:
    os.environ["CQLENG_ALLOW_SCHEMA_MANAGEMENT"]="1"


class Settings(BaseSettings):
    db_client_id:str=Field(...,env='clientID')
    db_client_secret:str=Field(...,env='clientSecret')

    class Config:
        env_file=".env"

@lru_cache
def get_settings():
    return Settings()
