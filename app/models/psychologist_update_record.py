from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base, MedicalRecord, Psychologist
from services.database import session


class PsychologistUpdateRecord(Base):
    __tablename__ = "psychologist_update_record"

    id: Mapped[int] = mapped_column(
        "id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True
    )

    psychologist_id: Mapped[int] = mapped_column(ForeignKey("psychologist.id"))
    psychologist: Mapped["Psychologist"] = relationship(back_populates="psychologist_update_records")
    
    medical_record_id: Mapped[int] = mapped_column(ForeignKey("medical_record.id"))
    medical_record: Mapped["MedicalRecord"] = relationship(back_populates="psychologist_update_records")

    def __init__(self, psychologist, medical_record):
        self.psychologist = psychologist
        self.medical_record = medical_record

    @classmethod
    def find_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()

    @classmethod
    def find_by_psychologist_id(cls, psychologist_id):
        return session.query(cls).filter_by(psychologist_id=psychologist_id).all()

    @classmethod
    def find_by_medical_record_id(cls, medical_record_id):
        return session.query(cls).filter_by(medical_record_id=medical_record_id).all()

    @classmethod
    def save_all(cls, psychologist_update_records):
        session.add_all(psychologist_update_records)
        session.commit()

    @classmethod
    def save(cls, psychologist_update_record):
        session.add(psychologist_update_record)
        session.commit()
