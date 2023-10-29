from sqlalchemy import ForeignKey, VARCHAR, func
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base, Professional
from services.database import session

from typing import List


class Doctor(Base):
    __tablename__ = "doctor"

    id: Mapped[int] = mapped_column(
        "id",
        MEDIUMINT,
        ForeignKey(Professional.id),
        nullable=False,
        autoincrement=True,
        primary_key=True,
    )

    crm: Mapped[str] = mapped_column("crm", VARCHAR(10), nullable=False, unique=True)
    professional: Mapped["Professional"] = relationship(back_populates="doctors")
    consultations: Mapped[List["Consultation"]] = relationship(
        back_populates="doctor", cascade="all, delete-orphan"
    )

    doctor_suggest_treatments: Mapped[List["DoctorSuggestTreatment"]] = relationship(
        back_populates="doctor", cascade="all, delete-orphan"
    )

    doctor_update_records: Mapped[List["DoctorUpdateRecord"]] = relationship(
        back_populates="doctor", cascade="all, delete-orphan"
    )

    def __init__(self, crm, professional, **kw):
        super().__init__(**kw)
        self.crm = crm
        self.professional = professional

    @classmethod
    def find_by_crm(cls, crm):
        return session.query(cls).filter_by(crm=crm).first()

    @classmethod
    def save_all(cls, doctors):
        session.add_all(doctors)
        session.commit()

    @classmethod
    def save(cls, doctor):
        session.add(doctor)
        session.commit()

    def __str__(self):
        return f"Doctor: {self.id}, {self.crm}"

    @classmethod
    def most_record_updates(cls):
        from models import DoctorUpdateRecord, Person, Professional
        query = (
        session.query(
            Person.name.label("Name"),
            func.count(DoctorUpdateRecord.id).label("Medical records updated"),
        )
        .join(cls, cls.id == DoctorUpdateRecord.doctor_id)
        .join(Professional, Professional.id == cls.id)
        .join(Person, Person.id == Professional.id)
        .group_by(cls.id)
        .order_by(func.count(DoctorUpdateRecord.id).desc())
    )
        return query.all()

    @classmethod
    def most_consultations(cls):
        from models import Consultation, Person
        query = (
        session.query(
                Person.name, func.count(Consultation.id).label("Consultation stats")
            )
            .join(Professional, Professional.id == Person.id)
            .join(cls, cls.id == Person.id)
            .join(Consultation, Consultation.doctor_id == cls.id)
            .group_by(Person.name)
            .limit(1)
        )

        result = query.first()
        print(result)