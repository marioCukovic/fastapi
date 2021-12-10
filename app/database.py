from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time
from .config import settings


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOSTNAME}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(
#             host="localhost", database="fastapi", user="postgres", password="postgres", cursor_factory=RealDictCursor
#         )
#         cursor = conn.cursor()
#         print("DB connection was successful")
#         break
#     except Exception as e:
#         print("Connecting to DB failed!")
#         print("Error:", e)
