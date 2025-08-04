from sqlalchemy.orm import Session
from app.feedback.repository import FeedbackRepository
from app.interaction.repository import InteractionRepository
from app.feedback.schema import FeedbackCreate, FeedbackResponse
from fastapi import HTTPException, status
from datetime import datetime
from typing import List

class FeedbackService:
    def __init__(self, db: Session):
        self.feedback_repo = FeedbackRepository(db)
        self.interaction_repo = InteractionRepository(db)

    def create_feedback(self, feedback_data: FeedbackCreate) -> FeedbackResponse:
        interaction = self.interaction_repo.get_interaction_by_id(feedback_data.interaction_id)
        if not interaction:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Interaction not found")
        
        feedback_date = feedback_data.feedback_date if feedback_data.feedback_date else datetime.now()
        db_feedback = self.feedback_repo.create_feedback(
            interaction_id=feedback_data.interaction_id,
            feedback_text=feedback_data.feedback_text,
            feedback_date=feedback_date
        )
        return FeedbackResponse.from_orm(db_feedback)

    def get_feedbacks_for_interaction(self, interaction_id: int) -> List[FeedbackResponse]:
        feedbacks = self.feedback_repo.get_feedbacks_by_interaction_id(interaction_id)
        return [FeedbackResponse.from_orm(feedback) for feedback in feedbacks]