from sqlalchemy import ForeignKey
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base, Treatment
from services.database import session


class TreatmentTreatsDisorder(Base):
    __tablename__ = "treatment_treats_disorder"

    id: Mapped[int] = mapped_column(
        "id", MEDIUMINT, nullable=False, primary_key=True, autoincrement=True
    )

    disorder_id: Mapped[int] = mapped_column(ForeignKey("disorder.id"))
    disorder: Mapped["Disorder"] = relationship(back_populates="treatment_treats_disorders")

    treatment_id: Mapped[int] = mapped_column(
        "treatment_id",
        MEDIUMINT,
        ForeignKey(Treatment.id),
        nullable=False,
        unique=False,
    )

    def __init__(self, disorder, treatment_id):
        self.disorder = disorder
        self.treatment_id = treatment_id

    @classmethod
    def find_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()

    @classmethod
    def find_by_patient_id(cls, patient_id):
        return session.query(cls).filter_by(patient_id=patient_id).all()

    @classmethod
    def find_by_treatment_id(cls, treatment_id):
        return session.query(cls).filter_by(treatment_id=treatment_id).all()

    @classmethod
    def save_all(cls, treatment_treats_disorders):
        session.add_all(treatment_treats_disorders)
        session.commit()

    @classmethod
    def save(cls, treatment_treats_disorder):
        session.add(treatment_treats_disorder)
        session.commit()
