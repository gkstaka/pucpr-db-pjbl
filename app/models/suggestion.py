from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base, Dosage


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

    def __init__(self, medicine, dosage, medical_record):
        self.medicine = medicine
        self.dosage = dosage
        self.medical_record = medical_record
