from typing import List

from sqlalchemy import ForeignKey, VARCHAR, CHAR, FLOAT, DATE
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base, Person
from services.database import session


class Professional(Base):
    __tablename__ = "professional"

    id: Mapped[int] = mapped_column(
        "id",
        MEDIUMINT,
        ForeignKey(Person.id),
        nullable=False,
        autoincrement=True,
        primary_key=True,
    )
    enrollment: Mapped[str] = mapped_column(
        "enrollment", CHAR(10), nullable=False, unique=True
    )
    salary: Mapped[float] = mapped_column("salary", FLOAT, nullable=False, unique=False)
    start_date: Mapped[str] = mapped_column(
        "start_date", DATE, nullable=False, unique=False
    )
    working_range: Mapped[str] = mapped_column(
        "working_range", VARCHAR(200), nullable=False, unique=False
    )
    speciality: Mapped[str] = mapped_column(
        "speciality", VARCHAR(200), nullable=False, unique=False
    )
    consultation_fee: Mapped[float] = mapped_column(
        "consultation_fee", FLOAT, nullable=True, unique=False
    )
    person: Mapped["Person"] = relationship(back_populates="people")
    doctors: Mapped[List["Doctor"]] = relationship(
        back_populates="professional", cascade="all, delete-orphan"
    )
    psychologists: Mapped[List["Psychologist"]] = relationship(
        back_populates="professional", cascade="all, delete-orphan"
    )

    def __init__(
        self,
        enrollment,
        salary,
        start_date,
        working_range,
        speciality,
        consultation_fee,
        person,
    ):
        self.enrollment = enrollment
        self.salary = salary
        self.start_date = start_date
        self.working_range = working_range
        self.speciality = speciality
        self.consultation_fee = consultation_fee
        self.person = person

    @classmethod
    def find_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()

    @classmethod
    def find_by_enrollment(cls, enrollment):
        return session.query(cls).filter_by(enrollment=enrollment).first()

    @classmethod
    def find_by_salary(cls, salary):
        return session.query(cls).filter_by(salary=salary).first()

    @classmethod
    def find_by_start_date(cls, start_date):
        return session.query(cls).filter_by(start_date=start_date).first()

    @classmethod
    def find_by_working_range(cls, working_range):
        return session.query(cls).filter_by(working_range=working_range).first()

    @classmethod
    def find_by_speciality(cls, speciality):
        return session.query(cls).filter_by(speciality=speciality).first()

    @classmethod
    def find_by_consultation_fee(cls, consultation_fee):
        return session.query(cls).filter_by(consultation_fee=consultation_fee).first()
