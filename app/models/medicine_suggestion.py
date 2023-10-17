from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT

from models import Base, Medicine, Dosage
from services.database import session


class MedicineSuggestion(Base):
    __tablename__ = "medicine_suggestion"

    id: Mapped[int] = mapped_column(
        "id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True
    )

    medicine_id: Mapped[int] = mapped_column(
        "medicine_id", MEDIUMINT, ForeignKey(Medicine.id), nullable=False, unique=False
    )

    dosage_id: Mapped[int] = mapped_column(
        "dosage_id", MEDIUMINT, ForeignKey(Dosage.id), nullable=False, unique=False
    )

    @classmethod
    def find_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()

    @classmethod
    def find_by_medicine_id(cls, medicine_id):
        return session.query(cls).filter_by(medicine_id=medicine_id).first()

    @classmethod
    def find_by_dosage_id(cls, dosage_id):
        return session.query(cls).filter_by(dosage_id=dosage_id).first()

    @classmethod
    def save_all(cls, medicine_suggestions):
        session.add_all(medicine_suggestions)
        session.commit()

    @classmethod
    def save(cls, medicine_suggestion):
        session.add(medicine_suggestion)
        session.commit()

    @classmethod
    def update_by_id(cls, id, new_data):
        record = session.query(cls).filter_by(id=id).first()
        if record:
            for key, value in new_data.items():
                setattr(record, key, value)
            session.commit()
        return record
