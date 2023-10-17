from datetime import datetime

from sqlalchemy import DATETIME, ForeignKey
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base, Patient
from services.database import session


class Consultation(Base):
    __tablename__ = "consultation"

    id: Mapped[int] = mapped_column(
        "id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True
    )
    time: Mapped[str] = mapped_column(
        "time", DATETIME, nullable=False, unique=False, default=datetime.now()
    )
    patient_id: Mapped[int] = mapped_column(ForeignKey("patient.id"))
    patient: Mapped["Patient"] = relationship(back_populates="consultations")

    def __init__(self, time, patient):
        self.time = time
        self.patient = patient

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
    def find_by_patient_id(cls, patient_id):
        return session.query(cls).filter_by(patient_id=patient_id).all()

