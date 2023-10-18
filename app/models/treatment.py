from datetime import datetime

from sqlalchemy import VARCHAR, DATETIME, ForeignKey
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base, Patient
from services.database import session

from typing import List

class Treatment(Base):
    __tablename__ = "treatment"

    id: Mapped[int] = mapped_column(
        "id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True
    )

    name: Mapped[str] = mapped_column(
        "name", VARCHAR(200), nullable=False, unique=False
    )

    start_date: Mapped[datetime] = mapped_column(
        "start_date", DATETIME, nullable=False, unique=False, default=datetime.now()
    )

    planned_end_date: Mapped[int] = mapped_column(
        "planned_end_date",
        DATETIME,
        nullable=False,
        unique=False,
        default=datetime.now(),
    )

    patient_id: Mapped[int] = mapped_column(
        ForeignKey("patient.id")
    )
    patient: Mapped["Patient"] = relationship(back_populates="treatment")
    
    treatment_treats_disorders: Mapped[List["TreatmentTreatsDisorder"]] = relationship(back_populates="treatment", cascade="all, delete-orphan")

    doctor_suggest_treatments: Mapped[List["DoctorSuggestTreatment"]] = relationship(
        back_populates="treatment", cascade="all, delete-orphan"
        )

    psychologist_helps_treatments: Mapped[List["PsychologistHelpsTreatment"]] = relationship(
        back_populates="treatment", cascade="all, delete-orphan"
        )

    medical_records: Mapped[List["MedicalRecord"]] = relationship(back_populates="treatment", cascade="all, delete-orphan")
    
    def __init__(self, name, start_date, planned_end_date, patient):
        self.name = name
        self.start_date = start_date
        self.planned_end_date = planned_end_date
        self.patient=patient

    @classmethod
    def find_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()

    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter_by(name=name).first()

    @classmethod
    def find_by_start_date(cls, start_date):
        return session.query(cls).filter_by(start_date=start_date).first()

    @classmethod
    def find_by_planned_end_date(cls, planned_end_date):
        return session.query(cls).filter_by(planned_end_date=planned_end_date).first()

    # @classmethod
    # def find_by_disorder_id(cls, disorder_id):
    #     return session.query(cls).filter_by(disorder_id=disorder_id).all()

    @classmethod
    def find_by_patient_id(cls, patient_id):
        return session.query(cls).filter_by(patient_id=patient_id).all()

    # @classmethod
    # def find_by_doctor_id(cls, doctor_id):
    #     return session.query(cls).filter_by(doctor_id=doctor_id).all()

    # @classmethod
    # def find_by_psychologist_id(cls, psychologist_id):
    #     return session.query(cls).filter_by(psychologist_id=psychologist_id).all()

    @classmethod
    def save_all(cls, treatments):
        session.add_all(treatments)
        session.commit()

    @classmethod
    def save(cls, treatment):
        session.add(treatment)
        session.commit()
