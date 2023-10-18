from datetime import datetime

from sqlalchemy import DATETIME, ForeignKey
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base
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
    
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctor.id"))
    doctor: Mapped["Doctor"] = relationship(back_populates="consultations")
    
    def __init__(self, time, patient, doctor):
        self.time = time
        self.patient = patient
        self.doctor = doctor

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

    @classmethod
    def find_by_doctor_id(cls, doctor_id):
        return session.query(cls).filter_by(doctor_id=doctor_id).all()

    @classmethod
    def save_all(cls, consultations):
        session.add_all(consultations)
        session.commit()

    @classmethod
    def save(cls, consultation):
        session.add(consultation)
        session.commit()
