from sqlalchemy import VARCHAR, ForeignKey
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base, Professional
from services.database import session

from typing import List


class Psychologist(Base):
    __tablename__ = "psychologist"

    id: Mapped[int] = mapped_column(
        "id",
        MEDIUMINT,
        ForeignKey(Professional.id),
        nullable=False,
        autoincrement=True,
        primary_key=True,
    )
    crp: Mapped[str] = mapped_column("crp", VARCHAR(10), nullable=False, unique=True)

    professional: Mapped["Professional"] = relationship(back_populates="psychologists")

    therapies: Mapped[List["Therapy"]] = relationship(back_populates="psychologist", cascade="all, delete-orphan")

    psychologist_helps_treatments: Mapped[List["PsychologistHelpsTreatment"]] = relationship(
        back_populates="psychologist", cascade="all, delete-orphan"
        )

    psychologist_update_records: Mapped[List["PsychologistUpdateRecord"]] = relationship(
        back_populates="psychologist", cascade="all, delete-orphan"
        )
    
    def __init__(self, crp, professional, **kw):
        super().__init__(**kw)
        self.crp = crp
        self.professional = professional

    @classmethod
    def find_by_crp(cls, crp):
        return session.query(cls).filter_by(crp=crp).first()

    @classmethod
    def save_all(cls, psychologists):
        session.add_all(psychologists)
        session.commit()

    @classmethod
    def save(cls, psychologist):
        session.add(psychologist)
        session.commit()
