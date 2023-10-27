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
    disorder: Mapped["Disorder"] = relationship(
        back_populates="treatment_treats_disorders"
    )

    treatment_id: Mapped[int] = mapped_column(ForeignKey("treatment.id"))
    treatment: Mapped["Treatment"] = relationship(
        back_populates="treatment_treats_disorders"
    )

    def __init__(self, disorder, treatment, **kw):
        super().__init__(**kw)
        self.disorder = disorder
        self.treatment = treatment

    @classmethod
    def find_by_disorder_id(cls, disorder_id):
        return session.query(cls).filter_by(disorder_id=disorder_id).all()

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


def update_by_id(cls, id, new_data):
    record = session.query(cls).filter_by(id=id).first()
    if record:
        for key, value in new_data.items():
            setattr(record, key, value)
        session.commit()
    return record
