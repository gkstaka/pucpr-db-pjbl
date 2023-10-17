from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column

from models import Base, MedicalRecord, Therapy
from services.database import session


class MedicalRecordIncludedTherapy:
    __tablename__ = "medical_record_included_therapy"

    id: Mapped[int] = mapped_column(
        "id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True
    )

    medical_record_id: Mapped[int] = mapped_column(
        "medical_record_id",
        MEDIUMINT,
        ForeignKey(MedicalRecord.id),
        nullable=False,
        unique=False,
    )

    therapy_id: Mapped[int] = mapped_column(
        "therapy_id", MEDIUMINT, ForeignKey(Therapy.id), nullable=False, unique=False
    )

    @classmethod
    def find_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()

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

    @classmethod
    def update_by_id(cls, id, new_data):
        record = session.query(cls).filter_by(id=id).first()
        if record:
            for key, value in new_data.items():
                setattr(record, key, value)
            session.commit()
        return record
