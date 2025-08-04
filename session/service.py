from sqlalchemy.orm import Session
from app.session.repository import SessionRepository
from app.user.service import UserService
from app.session.schema import SessionCreateRequest, SessionResponse, GroupedSessionsResponse, SessionUpdateRequest
from datetime import datetime, timedelta
from typing import List, Dict

class SessionService:
    def __init__(self, db: Session):
        self.session_repo = SessionRepository(db)
        self.user_service = UserService(db)

    def create_session(self, session_data: SessionCreateRequest) -> SessionResponse:
        user = self.user_service.create_user_if_not_exists(session_data) # Reusing UserCreate schema
        db_session = self.session_repo.create_session(user_id=user.user_id, session_name=session_data.session_name)
        return SessionResponse.from_orm(db_session)

    def get_sessions_grouped_by_user(self, user_id: int) -> GroupedSessionsResponse:
        sessions = self.session_repo.get_sessions_by_user_id(user_id)
        
        today = datetime.now().date()
        last_7_days = today - timedelta(days=7)
        last_30_days = today - timedelta(days=30)

        today_sessions: List[SessionResponse] = []
        last_7_days_sessions: List[SessionResponse] = []
        last_30_days_sessions: List[SessionResponse] = []

        for session in sessions:
            session_date = session.login_time.date()
            if session_date == today:
                today_sessions.append(SessionResponse.from_orm(session))
            elif last_7_days <= session_date < today:
                last_7_days_sessions.append(SessionResponse.from_orm(session))
            elif last_30_days <= session_date < today:
                last_30_days_sessions.append(SessionResponse.from_orm(session))
        
        return GroupedSessionsResponse(
            today=today_sessions,
            last_7_days=last_7_days_sessions,
            last_30_days=last_30_days_sessions
        )

    def delete_session(self, session_id: int) -> bool:
        return self.session_repo.delete_session(session_id)

    def update_session_name(self, session_id: int, session_data: SessionUpdateRequest) -> SessionResponse | None:
        updated_session = self.session_repo.update_session_name(session_id, session_data.session_name)
        return SessionResponse.from_orm(updated_session) if updated_session else None