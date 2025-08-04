from sqlalchemy.orm import Session
from app.db.models.interaction_model import Interaction
from typing import List

class InteractionRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_interactions_by_session_id(self, session_id: int) -> List[Interaction]:
        return self.db.query(Interaction).filter(Interaction.session_id == session_id).all()

    def create_interaction(self, session_id: int, user_id: int, message: str, response: str) -> Interaction:
        db_interaction = Interaction(
            session_id=session_id,
            user_id=user_id,
            message=message,
            response=response
        )
        self.db.add(db_interaction)
        self.db.commit()
        self.db.refresh(db_interaction)
        return db_interaction

    def get_interaction_by_id(self, interaction_id: int) -> Interaction | None:
        return self.db.query(Interaction).filter(Interaction.interaction_id == interaction_id).first()