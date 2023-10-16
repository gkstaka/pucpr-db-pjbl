from datetime import datetime, date
from typing import List

from sqlalchemy import ForeignKey, VARCHAR, CHAR, DATE, FLOAT, DATETIME
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base, Person


class Patient(Base):
    __tablename__ = "patient"

    id: Mapped[int] = mapped_column(
        "id",
        MEDIUMINT,
        ForeignKey(Person.id),
        nullable=False,
        autoincrement=True,
        primary_key=True,
    )
    weight: Mapped[float] = mapped_column("weight", FLOAT, nullable=False, unique=False)
    marital_status: Mapped[str] = mapped_column(
        "marital_status", VARCHAR(200), nullable=False, unique=False
    )
    profession: Mapped[str] = mapped_column(
        "profession", VARCHAR(200), nullable=False, unique=False
    )
    emergency_contact_name: Mapped[str] = mapped_column(
        "emergency_contact_name", VARCHAR(200), nullable=False, unique=False
    )
    emergency_contact_phone: Mapped[str] = mapped_column(
        "emergency_contact_phone", VARCHAR(14), nullable=False, unique=False
    )
    health_insurance: Mapped[str] = mapped_column(
        "health_insurance", VARCHAR(50), nullable=False, unique=False
    )
    hospitalization_date: Mapped[date] = mapped_column(
        "hospitalization_date",
        DATETIME,
        nullable=False,
        unique=False,
        default=datetime.now(),
    )
    person: Mapped["Person"] = relationship(back_populates="patients")
    consultations: Mapped[List["Consultation"]] = relationship(
        back_populates="patient", cascade="all, delete-orphan"
    )

    def __init__(
        self,
        weight,
        marital_status,
        profession,
        emergency_contact_name,
        emergency_contact_phone,
        health_insurance,
        hospitalization_date,
        person,
    ):
        self.weight = weight
        self.marital_status = marital_status
        self.profession = profession
        self.emergency_contact_name = emergency_contact_name
        self.emergency_contact_phone = emergency_contact_phone
        self.health_insurance = health_insurance
        self.hospitalization_date = hospitalization_date
        self.person = person
