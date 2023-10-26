from typing import List

from datetime import date
from sqlalchemy import VARCHAR, CHAR, INTEGER, DATE

from models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import MEDIUMINT

from services.database import session


class Person(Base):
    __tablename__ = "person"

    id: Mapped[int] = mapped_column(
        "id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True
    )
    name: Mapped[str] = mapped_column(
        "name", VARCHAR(200), nullable=False, unique=False
    )
    birth_date: Mapped[date] = mapped_column(
        "birth_date", DATE, nullable=False, unique=False
    )
    sex: Mapped[str] = mapped_column("sex", CHAR(1), nullable=False, unique=False)
    cpf: Mapped[str] = mapped_column("cpf", CHAR(11), nullable=False, unique=True)
    zip: Mapped[str] = mapped_column("zip", CHAR(8), nullable=True, unique=False)
    street: Mapped[str] = mapped_column(
        "street", VARCHAR(200), nullable=True, unique=False
    )
    street_number: Mapped[str] = mapped_column(
        "street_number", INTEGER, nullable=True, unique=False
    )
    complement: Mapped[str] = mapped_column(
        "complement", VARCHAR(200), nullable=True, unique=False
    )
    neighborhood: Mapped[str] = mapped_column(
        "neighborhood", VARCHAR(200), nullable=True, unique=False
    )
    city: Mapped[str] = mapped_column("city", VARCHAR(200), nullable=True, unique=False)
    state: Mapped[str] = mapped_column("state", CHAR(2), nullable=True, unique=False)
    country: Mapped[str] = mapped_column(
        "country", CHAR(3), nullable=True, unique=False
    )
    phone: Mapped[str] = mapped_column(
        "phone", VARCHAR(14), nullable=False, unique=True
    )
    email: Mapped[str] = mapped_column(
        "email", VARCHAR(50), nullable=False, unique=True
    )
    people: Mapped[List["Professional"]] = relationship(
        back_populates="person", cascade="all, delete-orphan"
    )
    patients: Mapped[List["Patient"]] = relationship(
        back_populates="person", cascade="all, delete-orphan"
    )

    def __init__(
        self,
        name,
        birth_date,
        sex,
        zip,
        cpf,
        street,
        street_number,
        complement,
        neighborhood,
        city,
        state,
        country,
        phone,
        email,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.name = name
        self.birth_date = birth_date
        self.sex = sex
        self.zip = zip
        self.cpf = cpf
        self.street = street
        self.street_number = street_number
        self.complement = complement
        self.neighborhood = neighborhood
        self.city = city
        self.state = state
        self.country = country
        self.phone = phone
        self.email = email

    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter_by(name=name).all()

    @classmethod
    def find_by_birth_date(cls, birth_date):
        return session.query(cls).filter_by(birth_date=birth_date).all()

    @classmethod
    def find_by_sex(cls, sex):
        return session.query(cls).filter_by(sex=sex).all()

    @classmethod
    def find_by_zip(cls, zip):
        return session.query(cls).filter_by(zip=zip).all()

    @classmethod
    def find_by_cpf(cls, cpf):
        return session.query(cls).filter_by(cpf=cpf).first()

    @classmethod
    def find_by_street(cls, street):
        return session.query(cls).filter_by(street=street).all()

    @classmethod
    def find_by_street_number(cls, street_number):
        return session.query(cls).filter_by(street_number=street_number).all()

    @classmethod
    def find_by_complement(cls, complement):
        return session.query(cls).filter_by(complement=complement).all()

    @classmethod
    def find_by_neighborhood(cls, neighborhood):
        return session.query(cls).filter_by(neighborhood=neighborhood).all()

    @classmethod
    def find_by_city(cls, city):
        return session.query(cls).filter_by(city=city).all()

    @classmethod
    def find_by_state(cls, state):
        return session.query(cls).filter_by(state=state).all()

    @classmethod
    def find_by_country(cls, country):
        return session.query(cls).filter_by(country=country).all()

    @classmethod
    def find_by_phone(cls, phone):
        return session.query(cls).filter_by(phone=phone).first()

    @classmethod
    def find_by_email(cls, email):
        return session.query(cls).filter_by(email=email).first()

    @classmethod
    def find_by_address(cls, street, street_number, neighborhood, city, state, country):
        return session.query(cls).filter_by(
            street=street,
            street_number=street_number,
            neighborhood=neighborhood,
            city=city,
            state=state,
            country=country
        ).all()

    @classmethod
    def save_all(cls, people):
        session.add_all(people)
        session.commit()

    @classmethod
    def save(cls, person):
        session.add(person)
        session.commit()
