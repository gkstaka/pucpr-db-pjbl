from typing import List

from sqlalchemy import VARCHAR
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base
from services.database import session


class Medicine(Base):
    __tablename__ = "medicine"

    id: Mapped[int] = mapped_column(
        "id", MEDIUMINT, nullable=False, autoincrement=True, primary_key=True
    )
    name: Mapped[str] = mapped_column("name", VARCHAR(200), nullable=False, unique=True)
    composition: Mapped[str] = mapped_column(
        "composition", VARCHAR(200), nullable=False, unique=True
    )
    usage_type: Mapped[int] = mapped_column(
        "usage_type", VARCHAR(50), nullable=False, unique=False
    )
    indication: Mapped[str] = mapped_column(
        "indication", VARCHAR(200), nullable=False, unique=False
    )
    contraindication: Mapped[str] = mapped_column(
        "contraindication", VARCHAR(200), nullable=False, unique=False
    )
    suggestions: Mapped[List["Suggestion"]] = relationship(
        back_populates="medicine", cascade="all, delete-orphan"
    )

    def __init__(
        self, name, composition, usage_type, indication, contraindication, **kw
    ):
        super().__init__(**kw)
        self.name = name
        self.composition = composition
        self.usage_type = usage_type
        self.indication = indication
        self.contraindication = contraindication

    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter_by(name=name).first()

    @classmethod
    def find_by_composition(cls, composition):
        return session.query(cls).filter_by(composition=composition).first()

    @classmethod
    def find_by_usage_type(cls, usage_type):
        return session.query(cls).filter_by(usage_type=usage_type).all()

    @classmethod
    def find_by_indication(cls, indication):
        return session.query(cls).filter_by(indication=indication).all()

    @classmethod
    def find_by_contraindication(cls, contraindication):
        return session.query(cls).filter_by(contraindication=contraindication).all()

    @classmethod
    def save_all(cls, medicines):
        session.add_all(medicines)
        session.commit()

    @classmethod
    def save(cls, medicine):
        session.add(medicine)
        session.commit()

    def __str__(self):
        return f"Medicine: {self.id}, {self.name}, {self.composition}, {self.usage_type}, {self.indication}, {self.contraindication}"
    