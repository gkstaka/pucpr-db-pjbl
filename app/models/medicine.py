from typing import List

from sqlalchemy import VARCHAR
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base


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

    def __init__(self, name, composition, usage_type, indication, contraindication):
        self.name = name
        self.composition = composition
        self.usage_type = usage_type
        self.indication = indication
        self.contraindication = contraindication
