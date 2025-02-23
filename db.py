from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engin = create_async_engine('sqlite+aiosqlite:///db.sqlite3', echo=True)
SessionDB = sessionmaker(bind=engin)


class Base(DeclarativeBase):
    pass
