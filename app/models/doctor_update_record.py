from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base, Doctor, MedicalRecord
from services.database import session


class DoctorUpdateRecord(Base):
    __tablename__ = "doctor_update_record"

    id: Mapped[int] = mapped_column(
        "id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True
    )

    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctor.id"))
    doctor: Mapped["Doctor"] = relationship(back_populates="doctor_update_records")

    medical_record_id: Mapped[int] = mapped_column(ForeignKey("medical_record.id"))
    medical_record: Mapped["MedicalRecord"] = relationship(
        back_populates="doctor_update_records"
    )

    def __init__(self, doctor, medical_record, **kw):
        super().__init__(**kw)
        self.doctor = doctor
        self.medical_record = medical_record

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

    def __str__(self):
        return f"Doctor Update Record: {self.id}, {self.doctor_id}, {self.medical_record_id}"
