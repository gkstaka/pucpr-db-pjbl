from sqlalchemy import VARCHAR, FLOAT
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column

from models import Base
from services.database import session


class Disorder(Base):
    __tablename__ = "disorder"

    id: Mapped[int] = mapped_column(
        "id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True
    )

    name: Mapped[str] = mapped_column("name", VARCHAR(200), nullable=False, unique=True)

    category: Mapped[str] = mapped_column(
        "category", VARCHAR(200), nullable=False, unique=False
    )

    symptoms: Mapped[str] = mapped_column(
        "symptoms", VARCHAR(200), nullable=False, unique=False
    )

    risk_factors: Mapped[str] = mapped_column(
        "risk_factors", VARCHAR(200), nullable=False, unique=False
    )

    prevalence: Mapped[str] = mapped_column(
        "prevalence", FLOAT, nullable=False, unique=False
    )

    @classmethod
    def find_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()

    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter_by(name=name).all()

    @classmethod
    def find_by_category(cls, category):
        return session.query(cls).filter_by(category=category).all()

    @classmethod
    def find_by_symptoms(cls, symptoms):
        return session.query(cls).filter_by(symptoms=symptoms).all()

    @classmethod
    def find_by_risk_factors(cls, risk_factors):
        return session.query(cls).filter_by(risk_factors=risk_factors).all()

    @classmethod
    def find_by_prevalence(cls, prevalence):
        return session.query(cls).filter_by(prevalence=prevalence).all()

    @classmethod
    def save_all(cls, disorders):
        session.add_all(disorders)
        session.commit()

    @classmethod
    def save(cls, disorder):
        session.add(disorder)
        session.commit()

    @classmethod
    def update_by_id(cls, id, new_data):
        record = session.query(cls).filter_by(id=id).first()
        if record:
            for key, value in new_data.items():
                setattr(record, key, value)
            session.commit()
        return record
