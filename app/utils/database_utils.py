from models import *
from services.database import engine


def create_db():
    Base.metadata.create_all(bind=engine)
