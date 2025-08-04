from sqlalchemy.orm import Session
from app.db.models.user_model import User
from app.user.schema import UserCreate

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.user_id == user_id).first()

    def get_user_by_email(self, email: str) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def create_user(self, user: UserCreate) -> User:
        db_user = User(email=user.email, username=user.username)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user