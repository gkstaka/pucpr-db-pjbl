from datetime import datetime

from sqlalchemy import ForeignKey, VARCHAR, DATETIME
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base, Patient, Doctor, Psychologist, Treatment, Medicine
from models.therapy import Therapy
from services.database import session


class MedicalRecord(Base):
    __tablename__ = "medical_record"

    id: Mapped[int] = mapped_column(
        "id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True
    )
    patient_id: Mapped[int] = mapped_column(
        "patient_id", MEDIUMINT, ForeignKey(Patient.id), nullable=False, unique=False
    )
    doctor_id: Mapped[int] = mapped_column(
        "doctor_id", MEDIUMINT, ForeignKey(Doctor.id), nullable=False, unique=False
    )
    psychologist_id: Mapped[int] = mapped_column(
        "psychologist_id",
        MEDIUMINT,
        ForeignKey(Psychologist.id),
        nullable=False,
        unique=False,
    )
    treatment_id: Mapped[int] = mapped_column(
        "treatment_id",
        MEDIUMINT,
        ForeignKey(Treatment.id),
        nullable=False,
        unique=False,
    )
    therapy_id: Mapped[int] = mapped_column(
        "therapy_id", MEDIUMINT, ForeignKey(Therapy.id), nullable=False, unique=False
    )
    record_date: Mapped[str] = mapped_column(
        "record_date", DATETIME, nullable=False, unique=False, default=datetime.now()
    )
    description: Mapped[str] = mapped_column(
        "description", VARCHAR(200), nullable=False, unique=False
    )
    suggestions: Mapped["Suggestion"] = relationship(
        back_populates="medical_record", cascade="all, delete-orphan"
    )

    @classmethod
    def find_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()

    @classmethod
    def find_by_patient_id(cls, patient_id):
        return session.query(cls).filter_by(patient_id=patient_id).all()

    @classmethod
    def find_by_doctor_id(cls, doctor_id):
        return session.query(cls).filter_by(doctor_id=doctor_id).all()

    @classmethod
    def find_by_psychologist_id(cls, psychologist_id):
        return session.query(cls).filter_by(psychologist_id=psychologist_id).all()

    @classmethod
    def find_by_treatment_id(cls, treatment_id):
        return session.query(cls).filter_by(treatment_id=treatment_id).all()

    @classmethod
    def find_by_therapy_id(cls, therapy_id):
        return session.query(cls).filter_by(therapy_id=therapy_id).all()

    @classmethod
    def find_by_record_date(cls, record_date):
        return session.query(cls).filter_by(record_date=record_date).all()

    @classmethod
    def find_by_description(cls, description):
        return session.query(cls).filter_by(description=description).all()
