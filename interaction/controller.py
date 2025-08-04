from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.interaction.service import InteractionService
from app.interaction.schema import InteractionCreate, InteractionResponse
from typing import List

router = APIRouter()

@router.get("/{session_id}/interactions", response_model=List[InteractionResponse])
def get_interactions(session_id: int, db: Session = Depends(get_db)):
    interaction_service = InteractionService(db)
    interactions = interaction_service.get_interactions_for_session(session_id)
    return interactions

@router.post("/{session_id}/interactions", response_model=InteractionResponse, status_code=status.HTTP_201_CREATED)
def create_interaction(session_id: int, interaction_data: InteractionCreate, db: Session = Depends(get_db)):
    interaction_service = InteractionService(db)
    new_interaction = interaction_service.create_interaction(session_id, interaction_data)
    return new_interaction