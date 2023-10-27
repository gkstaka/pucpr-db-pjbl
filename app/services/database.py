from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from urllib.parse import quote

instance = f"mysql+pymysql://root:vBst&Ebb5hw@localhost:3306/psychiatric_hospital"

if not database_exists(url=instance):
    create_database(url=instance)

engine = create_engine(url=instance, echo=True)
session = Session(bind=engine, autocommit=False, autoflush=True)
