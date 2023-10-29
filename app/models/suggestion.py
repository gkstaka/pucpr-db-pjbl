from sqlalchemy import ForeignKey, func
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base
from services.database import session


class Suggestion(Base):
    __tablename__ = "suggestion"

    id: Mapped[int] = mapped_column(
        "id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True
    )
    medicine_id: Mapped[int] = mapped_column(ForeignKey("medicine.id"))
    medicine: Mapped["Medicine"] = relationship(back_populates="suggestions")
    dosage_id: Mapped[int] = mapped_column(ForeignKey("dosage.id"))
    dosage: Mapped["Dosage"] = relationship(back_populates="suggestions")
    medical_record_id: Mapped[int] = mapped_column(ForeignKey("medical_record.id"))
    medical_record: Mapped["MedicalRecord"] = relationship(back_populates="suggestions")

    def __init__(self, medicine_id, dosage_id, medical_record_id, **kw):
        super().__init__(**kw)
        self.medicine_id = medicine_id
        self.dosage_id = dosage_id
        self.medical_record_id = medical_record_id

    @classmethod
    def find_by_medicine_id(cls, medicine_id):
        return session.query(cls).filter_by(medicine_id=medicine_id).all()

    @classmethod
    def find_by_dosage_id(cls, dosage_id):
        return session.query(cls).filter_by(dosage_id=dosage_id).all()

    @classmethod
    def find_by_medical_record_id(cls, medical_record_id):
        return session.query(cls).filter_by(medical_record_id=medical_record_id).all()

    @classmethod
    def save_all(cls, suggestions):
        session.add_all(suggestions)
        session.commit()

    @classmethod
    def save(cls, suggestion):
        session.add(suggestion)
        session.commit()

    def __str__(self):
        return f"Suggestion: {self.id}, {self.medicine_id}, {self.dosage_id}, {self.medical_record_id}"

    @classmethod
    def average_medication_taken(cls):
        from models import MedicalRecord
        return (
            session.query((func.count(cls.id) / func.count(MedicalRecord.id)).label("Average medication taken"))
            .join(MedicalRecord, MedicalRecord.id == cls.medical_record_id).scalar()
            )