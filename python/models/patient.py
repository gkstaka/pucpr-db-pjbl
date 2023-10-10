from datetime import datetime, date

from sqlalchemy import ForeignKey, VARCHAR, CHAR, DATE, FLOAT, DATETIME
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column

from models import Base, Person


class Patient(Base):
    __tablename__ = "patient"

    id: Mapped[int] = mapped_column("id",
                                    MEDIUMINT,
                                    ForeignKey(Person.id),
                                    nullable=False,
                                    autoincrement=True,
                                    primary_key=True)

    weight: Mapped[float] = mapped_column("weight",
                                          FLOAT,
                                          nullable=False,
                                          unique=False)

    marital_status: Mapped[str] = mapped_column("marital_status",
                                                VARCHAR(200),
                                                nullable=False,
                                                unique=False)

    profession: Mapped[str] = mapped_column("profession",
                                            VARCHAR(200),
                                            nullable=False,
                                            unique=False)

    emergency_contact_name: Mapped[str] = mapped_column("emergency_contact_name",
                                                        VARCHAR(200),
                                                        nullable=False,
                                                        unique=False)

    emergency_contact_phone: Mapped[str] = mapped_column("emergency_contact_phone",
                                                         CHAR(11),
                                                         nullable=False,
                                                         unique=False)

    health_insurance: Mapped[str] = mapped_column("health_insurance",
                                                  VARCHAR(50),
                                                  nullable=False,
                                                  unique=False)

    hospitalization_date: Mapped[date] = mapped_column("hospitalization_date",
                                                       DATETIME,
                                                       nullable=False,
                                                       unique=False,
                                                       default=datetime.now())
