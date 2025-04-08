from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

from core.settings import settings

db = settings.DataBase()

DATABASE_URL = f"{db.DATABASE_DEFAULT}+{db.DATABASE_BRAIN}://{db.POSTGRES_USER}:{db.POSTGRES_PASSWORD}@{db.POSTGRES_HOST}:{db.POSTGRES_PORT}/{db.POSTGRES_DB}"

engine = create_engine(url=DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
