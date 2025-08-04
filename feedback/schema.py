from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FeedbackBase(BaseModel):
    interaction_id: int
    feedback_text: str

class FeedbackCreate(FeedbackBase):
    feedback_date: Optional[datetime] = None

class FeedbackResponse(FeedbackBase):
    feedback_id: int
    feedback_date: datetime

    class Config:
        from_attributes = True