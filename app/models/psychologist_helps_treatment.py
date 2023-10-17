from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT
from models import Base, Psychologist, Treatment
from services.database import session


class PsychologistHelpsTreatment(Base):
    __tablename__ = "psychologist_helps_treatment"

    id: Mapped[int] = mapped_column(
        "id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True
    )

    psychologist_id: Mapped[int] = mapped_column(
        "doctor_id",
        MEDIUMINT,
        ForeignKey(Psychologist.id),
        nullable=False,
        unique=False,
    )

    treatment_id: Mapped[int] = mapped_column(
        "treatment_id",
        MEDIUMINT,
        ForeignKey(Treatment.id),
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
    def find_by_psychologist_id(cls, psychologist_id):
        return session.query(cls).filter_by(psychologist_id=psychologist_id).all()

    @classmethod
    def find_by_treatment_id(cls, treatment_id):
        return session.query(cls).filter_by(treatment_id=treatment_id).all()

    @classmethod
    def save_all(cls, psychologist_helps_treatments):
        session.add_all(psychologist_helps_treatments)
        session.commit()

    @classmethod
    def save(cls, psychologist_helps_treatment):
        session.add(psychologist_helps_treatment)
        session.commit()

    @classmethod
    def update_by_id(cls, id, new_data):
        record = session.query(cls).filter_by(id=id).first()
        if record:
            for key, value in new_data.items():
                setattr(record, key, value)
            session.commit()
        return record
