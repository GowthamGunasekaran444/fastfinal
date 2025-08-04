from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Setup SQLAlchemy engine using SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./chatbot.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create Base using declarative_base()
Base = declarative_base()