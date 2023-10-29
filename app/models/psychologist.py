from sqlalchemy import VARCHAR, ForeignKey, func
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship, aliased

from models import Base, Professional
from services.database import session

from typing import List


class Psychologist(Base):
    __tablename__ = "psychologist"

    id: Mapped[int] = mapped_column(
        "id",
        MEDIUMINT,
        ForeignKey(Professional.id),
        nullable=False,
        autoincrement=True,
        primary_key=True,
    )
    crp: Mapped[str] = mapped_column("crp", VARCHAR(10), nullable=False, unique=True)

    professional: Mapped["Professional"] = relationship(back_populates="psychologists")

    therapies: Mapped[List["Therapy"]] = relationship(
        back_populates="psychologist", cascade="all, delete-orphan"
    )

    psychologist_helps_treatments: Mapped[
        List["PsychologistHelpsTreatment"]
    ] = relationship(back_populates="psychologist", cascade="all, delete-orphan")

    psychologist_update_records: Mapped[
        List["PsychologistUpdateRecord"]
    ] = relationship(back_populates="psychologist", cascade="all, delete-orphan")

    def __init__(self, crp, professional, **kw):
        super().__init__(**kw)
        self.crp = crp
        self.professional = professional

    @classmethod
    def find_by_crp(cls, crp):
        return session.query(cls).filter_by(crp=crp).first()

    @classmethod
    def save_all(cls, psychologists):
        session.add_all(psychologists)
        session.commit()

    @classmethod
    def save(cls, psychologist):
        session.add(psychologist)
        session.commit()

    def __str__(self):
        return f"Psychologist: {self.id}, {self.crp}"

    @classmethod
    def count_patients_per_psy(cls):
        from models import Person, Patient, Treatment, PsychologistHelpsTreatment
        psychologist_person = aliased(Person)  
        query = (
        session.query(
            psychologist_person.name.label("Psychologist name"), 
            func.count(Patient.id).label("Number of Patients")
        )
        .join(Treatment, Treatment.patient_id == Patient.id)
        .join(
            PsychologistHelpsTreatment,
            PsychologistHelpsTreatment.treatment_id == Treatment.id,
        )
        .join(
            cls, PsychologistHelpsTreatment.psychologist_id == cls.id
        )
        .join(psychologist_person, cls.id == psychologist_person.id)
        .group_by(psychologist_person.name)
        .order_by(psychologist_person.name)
    )

        return query.all()

    @classmethod
    def most_record_updates(cls):
        from models import PsychologistUpdateRecord, Person, Professional
        query = (
        session.query(
            Person.name.label("Name"),
            func.count(PsychologistUpdateRecord.id).label("Medical records updated"),
        )
        .join(cls, cls.id == PsychologistUpdateRecord.psychologist_id)
        .join(Professional, Professional.id == cls.id)
        .join(Person, Person.id == Professional.id)
        .group_by(cls.id)
        .order_by(func.count(PsychologistUpdateRecord.id).desc())
    )
        return query.all()