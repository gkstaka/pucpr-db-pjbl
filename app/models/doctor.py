from sqlalchemy import ForeignKey, VARCHAR
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base, Professional
from services.database import session

from typing import List
class Doctor(Base):
    __tablename__ = "doctor"

    id: Mapped[int] = mapped_column(
        "id",
        MEDIUMINT,
        ForeignKey(Professional.id),
        nullable=False,
        autoincrement=True,
        primary_key=True,
    )

    crm: Mapped[str] = mapped_column("crm", VARCHAR(10), nullable=False, unique=True)
    professional: Mapped["Professional"] = relationship(back_populates="doctors")
    consultations: Mapped[List["Consultation"]] = relationship(
        back_populates="doctor", cascade="all, delete-orphan"
        )
    def __init__(self, crm, professional):
        self.crm = crm
        self.professional = professional

    @classmethod
    def find_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()

    @classmethod
    def find_by_crm(cls, crm):
        return session.query(cls).filter_by(crm=crm).first()

    @classmethod
    def save_all(cls, doctors):
        session.add_all(doctors)
        session.commit()

    @classmethod
    def save(cls, doctor):
        session.add(doctor)
        session.commit()
