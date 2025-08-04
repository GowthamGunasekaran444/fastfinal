from sqlalchemy.orm import Session
from app.interaction.repository import InteractionRepository
from app.session.repository import SessionRepository
from app.interaction.schema import InteractionCreate, InteractionResponse
from fastapi import HTTPException, status
from typing import List

class InteractionService:
    def __init__(self, db: Session):
        self.interaction_repo = InteractionRepository(db)
        self.session_repo = SessionRepository(db)

    def get_interactions_for_session(self, session_id: int) -> List[InteractionResponse]:
        interactions = self.interaction_repo.get_interactions_by_session_id(session_id)
        return [InteractionResponse.from_orm(interaction) for interaction in interactions]

    def create_interaction(self, session_id: int, interaction_data: InteractionCreate) -> InteractionResponse:
        session = self.session_repo.get_session_by_id(session_id)
        if not session:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")
        
        db_interaction = self.interaction_repo.create_interaction(
            session_id=session_id,
            user_id=session.user_id, # Link interaction to user via session
            message=interaction_data.message,
            response=interaction_data.response
        )
        return InteractionResponse.from_orm(db_interaction)