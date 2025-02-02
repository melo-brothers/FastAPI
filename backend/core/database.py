from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from backend.settings import SQLALCHEMY_DATABASE_URL

if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def create_db_schema(engine):
    with SessionLocal() as db:
        Base.metadata.create_all(engine, checkfirst=True)
        db.commit()

if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    print("Creating tables...")
    create_db_schema(engine)
