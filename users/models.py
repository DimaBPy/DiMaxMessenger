import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.schema import CreateTable

from db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    time_stamp = Column(
        DateTime, default=datetime.datetime.now(tz=datetime.timezone.utc)
    )
    user_ip = Column(String)
    user_client = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)

    def __repr__(self):
        return (f"User(id={self.id}, username={self.username}, "
                f"email={self.email}, is_active={self.is_active}, "
                f"is_superuser={self.is_superuser}, "
                f"is_verified={self.is_verified})")

    def __str__(self):
        return self.username


if __name__ == '__main__':
    print(CreateTable(User.__table__))
