from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    created_time = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True) # 1/0 (User status Active/deactive)

    sessions = relationship("Session", back_populates="user")
    interactions = relationship("Interaction", back_populates="user")