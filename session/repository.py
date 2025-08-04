from sqlalchemy.orm import Session
from app.db.models.session_model import Session
from datetime import datetime, timedelta
from typing import List, Optional

class SessionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_session(self, user_id: int, session_name: Optional[str] = None) -> Session:
        db_session = Session(user_id=user_id, session_name=session_name)
        self.db.add(db_session)
        self.db.commit()
        self.db.refresh(db_session)
        return db_session

    def get_session_by_id(self, session_id: int) -> Session | None:
        return self.db.query(Session).filter(Session.session_id == session_id).first()

    def get_sessions_by_user_id(self, user_id: int) -> List[Session]:
        return self.db.query(Session).filter(Session.user_id == user_id).all()

    def delete_session(self, session_id: int):
        session = self.db.query(Session).filter(Session.session_id == session_id).first()
        if session:
            self.db.delete(session)
            self.db.commit()
            return True
        return False

    def update_session_name(self, session_id: int, new_session_name: str) -> Session | None:
        session = self.db.query(Session).filter(Session.session_id == session_id).first()
        if session:
            session.session_name = new_session_name
            self.db.commit()
            self.db.refresh(session)
            return session
        return None