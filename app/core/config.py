from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Благотворительный фонд поддержки котов'
    database_url: str
    secret: str

    class Config:
        env_file = '.env'


settings = Settings()
