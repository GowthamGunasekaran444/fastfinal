from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class Feedback(Base):
    __tablename__ = "feedback"

    feedback_id = Column(Integer, primary_key=True, index=True)
    interaction_id = Column(Integer, ForeignKey("interactions.interaction_id"), nullable=False)
    feedback_text = Column(String, nullable=False) # User's feedback or comments
    feedback_date = Column(DateTime(timezone=True), server_default=func.now()) # Date and time of feedback submission

    interaction = relationship("Interaction", back_populates="feedbacks")