from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class Interaction(Base):
    __tablename__ = "interactions"

    interaction_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False) # Added user_id as per image
    session_id = Column(Integer, ForeignKey("sessions.session_id"), nullable=False)
    message = Column(String, nullable=False) # User message to the chatbot
    response = Column(String, nullable=False) # Chatbot's response
    interaction_date = Column(DateTime(timezone=True), server_default=func.now()) # Date and time of the interaction

    session = relationship("Session", back_populates="interactions")
    user = relationship("User", back_populates="interactions")
    feedbacks = relationship("Feedback", back_populates="interaction", cascade="all, delete-orphan")