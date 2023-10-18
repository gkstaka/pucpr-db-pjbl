from datetime import datetime

from sqlalchemy import DATETIME, ForeignKey, VARCHAR, INTEGER
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base, Patient, Psychologist, Treatment
from services.database import session

from typing import List
class Therapy(Base):
    __tablename__ = "therapy"

    id: Mapped[int] = mapped_column(
        "id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True
    )

    time: Mapped[str] = mapped_column(
        "time", DATETIME, nullable=False, unique=False, default=datetime.now()
    )

    purpose: Mapped[int] = mapped_column(
        "purpose", VARCHAR(200), nullable=False, unique=True
    )

    capacity: Mapped[int] = mapped_column(
        "capacity", INTEGER, nullable=False, unique=False
    )

    psychologist_id: Mapped[int] = mapped_column(ForeignKey(Psychologist.id))
    psychologist: Mapped["Psychologist"] = relationship(back_populates="therapies")

    medical_record_included_therapies: Mapped[List["MedicalRecordIncludedTherapy"]] = relationship(
        back_populates="therapy", cascade="all, delete-orphan"
        )

    
    def __init__(self, time, purpose, capacity, psychologist):
        self.time = time
        self.purpose = purpose
        self.capacity = capacity
        self.psychologist = psychologist

    @classmethod
    def find_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()

    @classmethod
    def find_by_time(cls, time):
        return session.query(cls).filter_by(time=time).all()

    @classmethod
    def find_by_purpose(cls, purpose):
        return session.query(cls).filter_by(purpose=purpose).first()

    @classmethod
    def find_by_capacity(cls, capacity):
        return session.query(cls).filter_by(capacity=capacity).all()

    @classmethod
    def find_by_psychologist_id(cls, psychologist_id):
        return session.query(cls).filter_by(psychologist_id=psychologist_id).all()

    @classmethod
    def save_all(cls, therapies):
        session.add_all(therapies)
        session.commit()

    @classmethod
    def save(cls, therapy):
        session.add(therapy)
        session.commit()
