from sqlalchemy import ForeignKey, CHAR
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column

from models import Base, Professional


class Doctor(Base):
    __tablename__ = "doctor"

    id: Mapped[int] = mapped_column("id",
                                    MEDIUMINT,
                                    ForeignKey(Professional.id),
                                    nullable=False,
                                    autoincrement=True,
                                    primary_key=True)

    crm: Mapped[str] = mapped_column("crm",
                                     CHAR(10),
                                     nullable=False,
                                     unique=True)
