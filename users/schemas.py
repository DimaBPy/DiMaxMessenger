from pydantic import BaseModel, EmailStr, Field


class CreateUser(BaseModel):
    username: str = Field(description='ваш ник', max_length=20, min_length=2)
    email: EmailStr | None = None
    hashed_password: str


class CreateMessage(BaseModel):
    text: str
