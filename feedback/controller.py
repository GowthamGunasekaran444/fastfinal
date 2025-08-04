from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.feedback.service import FeedbackService
from app.feedback.schema import FeedbackCreate, FeedbackResponse
from typing import List

router = APIRouter()

@router.post("", response_model=FeedbackResponse, status_code=status.HTTP_201_CREATED)
def create_feedback(feedback_data: FeedbackCreate, db: Session = Depends(get_db)):
    feedback_service = FeedbackService(db)
    new_feedback = feedback_service.create_feedback(feedback_data)
    return new_feedback

@router.get("/{interaction_id}", response_model=List[FeedbackResponse])
def get_feedbacks_by_interaction(interaction_id: int, db: Session = Depends(get_db)):
    feedback_service = FeedbackService(db)
    feedbacks = feedback_service.get_feedbacks_for_interaction(interaction_id)
    return feedbacks