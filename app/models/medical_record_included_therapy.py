from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base, MedicalRecord, Therapy
from services.database import session


class MedicalRecordIncludedTherapy(Base):
    __tablename__ = "medical_record_included_therapy"

    id: Mapped[int] = mapped_column(
        "id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True
    )

    medical_record_id: Mapped[int] = mapped_column(
        ForeignKey("medical_record.id"),
    )
    medical_record: Mapped["MedicalRecord"] = relationship(
        back_populates="medical_record_included_therapies"
    )

    therapy_id: Mapped[int] = mapped_column(
        ForeignKey("therapy.id"),
    )
    therapy: Mapped["Therapy"] = relationship(
        back_populates="medical_record_included_therapies"
    )

    def __init__(self, medical_record, therapy, **kw):
        super().__init__(**kw)
        self.medical_record = medical_record
        self.therapy = therapy

    @classmethod
    def find_by_medical_record_id(cls, medical_record_id):
        return session.query(cls).filter_by(medical_record_id=medical_record_id).all()

    @classmethod
    def find_by_therapy_id(cls, therapy_id):
        return session.query(cls).filter_by(therapy_id=therapy_id).all()

    @classmethod
    def save_all(cls, medical_record_included_therapies):
        session.add_all(medical_record_included_therapies)
        session.commit()

    @classmethod
    def save(cls, medical_record_included_therapy):
        session.add(medical_record_included_therapy)
        session.commit()
