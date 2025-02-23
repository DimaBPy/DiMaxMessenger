from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncAttrs
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase

engin = create_async_engine('sqlite+aiosqlite:///db.sqlite3', echo=True)
SessionDB = async_sessionmaker(engin, expire_on_commit=False)



class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True