from pydantic import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):

    APP_NAME: str = Field(default="APP_NAME", env="APP_NAME")
    APP_DESCRIPTION: str = Field(default="APP_DESCRIPTION", env="APP_DESCRIPTION")
    DATABASE_URI: str = Field(env="DATABASE_URI")

settings = AppSettings(_env_file='local.env', _env_file_encoding='utf-8')
 