from sqlalchemy.orm import Session
from app.user.repository import UserRepository
from app.user.schema import UserCreate, UserResponse

class UserService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)

    def get_user_by_id(self, user_id: int) -> UserResponse | None:
        user = self.user_repo.get_user_by_id(user_id)
        return UserResponse.from_orm(user) if user else None

    def get_user_by_email(self, email: str) -> UserResponse | None:
        user = self.user_repo.get_user_by_email(email)
        return UserResponse.from_orm(user) if user else None

    def create_user_if_not_exists(self, user_data: UserCreate) -> UserResponse:
        user = self.user_repo.get_user_by_email(user_data.email)
        if not user:
            user = self.user_repo.create_user(user_data)
        return UserResponse.from_orm(user)