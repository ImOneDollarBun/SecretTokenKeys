from core.dbCore.main import Base, engine
from sqlalchemy import Column, String, func, DateTime, Integer, JSON


class Logs(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    at_time = Column(DateTime, server_default=func.now())
    level = Column(String)
    message = Column(String)
    context = Column(JSON)


Base.metadata.create_all(bind=engine)
