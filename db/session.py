from sqlalchemy.orm import sessionmaker
from app.db.base import engine
from typing import Generator

# Setup DB session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    """
    Dependency to get a database session.
    Yields a session and closes it after the request is finished.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()