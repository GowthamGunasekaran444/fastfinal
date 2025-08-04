from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Dict

class SessionBase(BaseModel):
    session_name: Optional[str] = None

class SessionCreateRequest(SessionBase):
    email: str
    user_id: Optional[str] = None

class SessionUpdateRequest(SessionBase):
    session_name: str

class SessionResponse(SessionBase):
    session_id: int
    user_id: int
    login_time: datetime
    logout_time: Optional[datetime] = None
    active_status: bool

    class Config:
        from_attributes = True

class GroupedSessionsResponse(BaseModel):
    today: List[SessionResponse]
    last_7_days: List[SessionResponse]
    last_30_days: List[SessionResponse]