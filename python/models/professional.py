from sqlalchemy import ForeignKey, VARCHAR, CHAR, FLOAT, DATE
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column

from models import Base, Person


class Professional(Base):
    __tablename__ = "professional"

    id: Mapped[int] = mapped_column("id",
                                    MEDIUMINT,
                                    ForeignKey(Person.id),
                                    nullable=False,
                                    autoincrement=True,
                                    primary_key=True)

    enrollment: Mapped[str] = mapped_column("enrollment",
                                            CHAR(10),
                                            nullable=False,
                                            unique=True)

    salary: Mapped[float] = mapped_column("salary",
                                          FLOAT,
                                          nullable=False,
                                          unique=False)

    start_date: Mapped[str] = mapped_column("start_date",
                                            DATE,
                                            nullable=False,
                                            unique=False)

    working_range: Mapped[str] = mapped_column("working_range",
                                               VARCHAR(200),
                                               nullable=False,
                                               unique=False)

    speciality: Mapped[str] = mapped_column("speciality",
                                            VARCHAR(200),
                                            nullable=False,
                                            unique=False)

    consultation_fee: Mapped[float] = mapped_column("consultation_fee",
                                                    FLOAT,
                                                    nullable=True,
                                                    unique=False)
