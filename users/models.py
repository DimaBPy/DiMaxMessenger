from time import tzset

from sqlalchemy import (Column, Integer, String, Boolean, DateTime, ForeignKey,
                        SmallInteger, func)
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import relationship, DeclarativeBase
from sqlalchemy.schema import CreateTable

from database.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True, nullable=True,
                   default=None)
    hashed_password = Column(String)
    timestamp = Column(DateTime, server_default=func.now())
    user_ip = Column(String, default=None)
    user_client = Column(String, nullable=True)
    is_active = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)

    message = relationship('Message', back_populates='user')

    def __repr__(self):
        return (f"User(id={self.id}, username={self.username}, "
                f"email={self.email}, is_active={self.is_active}, "
                f"is_superuser={self.is_superuser}, "
                f"is_verified={self.is_verified})")

    def __str__(self):
        return self.username


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    timestamp = Column(DateTime, server_default=func.now())
    to_user = Column(SmallInteger)
    from_user = Column(SmallInteger)
    is_read = Column(Boolean, default=False)
    is_received = Column(Boolean, default=False)
    user = relationship(User, back_populates='message')

    def __repr__(self):
        return (f"Message(id={self.id}, text={self.text}, "
                f"user_id={self.user})")

    def __str__(self):
        return self.text


if __name__ == '__main__':
    print(CreateTable(User.__table__))
    print(CreateTable(Message.__table__))
