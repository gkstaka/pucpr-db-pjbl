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
    dose_quantity: Mapped[str] = mapped_column(
        "dose_quantity", VARCHAR(50), nullable=False, unique=False
    )
    dose_frequency: Mapped[str] = mapped_column(
        "dose_frequency", VARCHAR(50), nullable=False, unique=False
    )
    suggestions: Mapped["Suggestion"] = relationship(
        back_populates="dosage", cascade="all, delete-orphan"
    )

    def __init__(self, dose_quantity, dose_frequency, **kw):
        super().__init__(**kw)
        self.dose_quantity = dose_quantity
        self.dose_frequency = dose_frequency

    @classmethod
    def find_by_dose_quantity(cls, dose_quantity):
        return session.query(cls).filter_by(dose_quantity=dose_quantity).all()

    @classmethod
    def find_by_dose_frequency(cls, dose_frequency):
        return session.query(cls).filter_by(dose_frequency=dose_frequency).all()

    @classmethod
    def save_all(cls, dosage_list):
        session.add_all(dosage_list)
        session.commit()

    @classmethod
    def save(cls, dosage):
        session.add(dosage)
        session.commit()

    def __str__(self):
        return f"Dosage: {self.id}, {self.dose_quantity}, {self.dose_frequency}"