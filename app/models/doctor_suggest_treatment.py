from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT
from models import Base, Doctor, Treatment
from services.database import session


class DoctorSuggestTreatment(Base):
    __tablename__ = "doctor_suggest_treatment"

    id: Mapped[int] = mapped_column(
        "id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True
    )

    doctor_id: Mapped[int] = mapped_column(
        "doctor_id", MEDIUMINT, ForeignKey(Doctor.id), nullable=False, unique=False
    )

    treatment_id: Mapped[int] = mapped_column(
        "treatment_id",
        MEDIUMINT,
        ForeignKey(Treatment.id),
        nullable=False,
        unique=False,
    )

    def __init__(self, doctor_id, treatment_id):
        self.doctor_id = doctor_id
        self.treatment_id = treatment_id

    @classmethod
    def find_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()

    @classmethod
    def find_by_doctor_id(cls, doctor_id):
        return session.query(cls).filter_by(doctor_id=doctor_id).all()

    @classmethod
    def find_by_treatment_id(cls, treatment_id):
        return session.query(cls).filter_by(treatment_id=treatment_id).all()

    @classmethod
    def save_all(cls, doctor_treatment_list):
        session.add_all(doctor_treatment_list)
        session.commit()

    @classmethod
    def save(cls, doctor_treatment):
        session.add(doctor_treatment)
        session.commit()

    @classmethod
    def update_by_id(cls, id, new_data):
        record = session.query(cls).filter_by(id=id).first()
        if record:
            for key, value in new_data.items():
                setattr(record, key, value)
            session.commit()
        return record
