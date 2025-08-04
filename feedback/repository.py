from sqlalchemy.orm import Session
from app.db.models.feedback_model import Feedback
from datetime import datetime
from typing import List

class FeedbackRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_feedback(self, interaction_id: int, feedback_text: str, feedback_date: datetime) -> Feedback:
        db_feedback = Feedback(
            interaction_id=interaction_id,
            feedback_text=feedback_text,
            feedback_date=feedback_date
        )
        self.db.add(db_feedback)
        self.db.commit()
        self.db.refresh(db_feedback)
        return db_feedback

    def get_feedbacks_by_interaction_id(self, interaction_id: int) -> List[Feedback]:
        return self.db.query(Feedback).filter(Feedback.interaction_id == interaction_id).all()