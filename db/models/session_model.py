from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class Session(Base):
    __tablename__ = "sessions"

    session_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    session_name = Column(String, nullable=True) # Assuming session_name is optional based on image.
    login_time = Column(DateTime(timezone=True), server_default=func.now())
    logout_time = Column(DateTime(timezone=True), nullable=True) # Date/Time when the session ended
    active_status = Column(Boolean, default=True) # 1/0 Whether the session is currently active

    user = relationship("User", back_populates="sessions")
    interactions = relationship("Interaction", back_populates="session", cascade="all, delete-orphan")