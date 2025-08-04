from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class InteractionBase(BaseModel):
    message: str
    response: str

class InteractionCreate(InteractionBase):
    pass

class InteractionResponse(InteractionBase):
    interaction_id: int
    session_id: int
    user_id: int
    interaction_date: datetime

    class Config:
        from_attributes = True