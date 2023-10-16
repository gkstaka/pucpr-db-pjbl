from sqlalchemy import ForeignKey, VARCHAR
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models import Base, Professional


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

    def __init__(self, crm, professional):
        self.crm = crm
        self.professional = professional
