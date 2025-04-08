import os
from dotenv import load_dotenv

load_dotenv()  # Загружает переменные из .env в окружение

class Settings:
    class DataBase:
        DATABASE_BRAIN = 'psycopg2'
        DATABASE_DEFAULT = 'postgresql'

        POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
        POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
        POSTGRES_DB = os.getenv("POSTGRES_DB", "mydatabase")
        POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
        POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")

    class Global:
        default_time = int(os.getenv("DEFAULT_TTL", 3600))

    class Redis:
        HOST = os.getenv("REDIS_HOST", "localhost")
        PORT = int(os.getenv("REDIS_PORT", "6379"))

    class App:
        APP_PORT = int(os.getenv("APP_PORT", "8000"))


settings = Settings()
