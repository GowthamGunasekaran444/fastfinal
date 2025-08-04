from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.session.service import SessionService
from app.session.schema import SessionCreateRequest, SessionResponse, GroupedSessionsResponse, SessionUpdateRequest

router = APIRouter()

@router.post("", response_model=SessionResponse, status_code=status.HTTP_201_CREATED)
def create_session(session_data: SessionCreateRequest, db: Session = Depends(get_db)):
    session_service = SessionService(db)
    new_session = session_service.create_session(session_data)
    return new_session

@router.get("/{user_id}", response_model=GroupedSessionsResponse)
def get_sessions_by_user(user_id: int, db: Session = Depends(get_db)):
    session_service = SessionService(db)
    grouped_sessions = session_service.get_sessions_grouped_by_user(user_id)
    return grouped_sessions

@router.delete("/{session_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_session(session_id: int, db: Session = Depends(get_db)):
    session_service = SessionService(db)
    if not session_service.delete_session(session_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")
    return

@router.put("/{session_id}", response_model=SessionResponse)
def update_session_name(session_id: int, session_data: SessionUpdateRequest, db: Session = Depends(get_db)):
    session_service = SessionService(db)
    updated_session = session_service.update_session_name(session_id, session_data)
    if not updated_session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")
    return updated_session