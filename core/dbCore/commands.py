from core.dbCore.main import SessionLocal
from core.dbCore.models import Logs

from sqlalchemy import select

session = SessionLocal()


def add_log(data: Logs):
    session.add(data)
    session.commit()
    session.refresh(data)

