from sqlalchemy import CHAR, ForeignKey
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base, Professional


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
    crp: Mapped[str] = mapped_column("crp", CHAR(10), nullable=False, unique=True)
    professional: Mapped["Professional"] = relationship(back_populates="psychologists")

    def __init__(self, crp, professional):
        self.crp = crp
        self.professional = professional
