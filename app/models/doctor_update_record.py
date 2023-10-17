from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column

from models import Base, Doctor, MedicalRecord
from services.database import session


class DoctorUpdateRecord(Base):
    __tablename__ = "doctor_update_record"

    id: Mapped[int] = mapped_column(
        "id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True
    )

    doctor_id: Mapped[int] = mapped_column(
        "doctor_id", MEDIUMINT, ForeignKey(Doctor.id), nullable=False, unique=False
    )

    medical_record_id: Mapped[int] = mapped_column(
        "medical_record_id",
        MEDIUMINT,
        ForeignKey(MedicalRecord.id),
        nullable=False,
        unique=False,
    )

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
    def find_by_medical_record_id(cls, medical_record_id):
        return session.query(cls).filter_by(medical_record_id=medical_record_id).all()

    @classmethod
    def save_all(cls, doctor_update_record_list):
        session.add_all(doctor_update_record_list)
        session.commit()

    @classmethod
    def save(cls, doctor_update_record):
        session.add(doctor_update_record)
        session.commit()
