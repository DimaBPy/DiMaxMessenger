from db import SessionDB


async def get_db():
    db = SessionDB()
    try:
        yield db
    finally:
        db.close()