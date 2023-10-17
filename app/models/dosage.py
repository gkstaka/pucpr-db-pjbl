from sqlalchemy import VARCHAR
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base
from services.database import session


class Dosage(Base):
    __tablename__ = "dosage"

    id: Mapped[int] = mapped_column(
        "id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True
    )
    dose_quantity: Mapped[int] = mapped_column(
        "dose_quantity", VARCHAR(50), nullable=False, unique=False
    )
    dose_frequency: Mapped[int] = mapped_column(
        "dose_frequency", VARCHAR(50), nullable=False, unique=False
    )
    suggestions: Mapped["Suggestion"] = relationship(
        back_populates="dosage", cascade="all, delete-orphan"
    )

    def __init__(self, dose_quantity, dose_frequency):
        self.dose_quantity = dose_quantity
        self.dose_frequency = dose_frequency

    @classmethod
    def find_all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter_by(id=id).first()

    @classmethod
    def find_by_dose_quantity(cls, dose_quantity):
        return session.query(cls).filter_by(dose_quantity=dose_quantity).all()

    @classmethod
    def find_by_dose_frequency(cls, dose_frequency):
        return session.query(cls).filter_by(dose_frequency=dose_frequency).all()
