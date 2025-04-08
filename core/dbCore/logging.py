import functools
import logging
from core.dbCore.main import SessionLocal
from core.dbCore.models import Logs


logger = logging.getLogger(__name__)


def log_action(level="INFO", msg=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log_msg = msg or f"Function {func.__name__} called"
            session = SessionLocal()
            log = Logs(
                level=level,
                message=log_msg,
                context={"args": str(args), "kwargs": str(kwargs)}
            )
            session.add(log)
            session.commit()
            session.close()

            try:
                result = func(*args, **kwargs)
            except Exception as e:
                logger.error(f"Error in {func.__name__}: {str(e)}")
                raise e

            return result

        return wrapper

    return decorator
