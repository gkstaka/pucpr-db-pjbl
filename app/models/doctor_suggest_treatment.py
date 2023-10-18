from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import MEDIUMINT
from models import Base, Doctor, Treatment
from services.database import session


class DoctorSuggestTreatment(Base):
    __tablename__ = "doctor_suggest_treatment"

    id: Mapped[int] = mapped_column(
        "id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True
    )

    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctor.id"))
    doctor: Mapped["Doctor"] = relationship(back_populates="doctor_suggest_treatments")
    
    treatment_id: Mapped[int] = mapped_column(ForeignKey("treatment.id"))
    treatment: Mapped["Treatment"] = relationship(back_populates="doctor_suggest_treatments")

    def __init__(self, doctor, treatment):
        self.doctor = doctor
        self.treatment = treatment

    @classmethod
    def find_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()

    @classmethod
    def find_by_doctor_id(cls, doctor_id):
        return session.query(cls).filter_by(doctor_id=doctor_id).all()

    @classmethod
    def find_by_treatment_id(cls, treatment_id):
        return session.query(cls).filter_by(treatment_id=treatment_id).all()

    @classmethod
    def save_all(cls, doctor_treatment_list):
        session.add_all(doctor_treatment_list)
        session.commit()

    @classmethod
    def save(cls, doctor_treatment):
        session.add(doctor_treatment)
        session.commit()
