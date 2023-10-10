from sqlalchemy import VARCHAR, CHAR, INTEGER, DATE
from datetime import datetime, date
from models import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import MEDIUMINT


class Person(Base):
    __tablename__ = "person"

    id: Mapped[int] = mapped_column("id",
                                    MEDIUMINT,
                                    nullable=False,
                                    autoincrement=True,
                                    primary_key=True)

    name: Mapped[str] = mapped_column("name",
                                      VARCHAR(200),
                                      nullable=False,
                                      unique=False)

    birth_date: Mapped[date] = mapped_column("birth_date",
                                             DATE,
                                             nullable=False,
                                             unique=False)

    sex: Mapped[str] = mapped_column("sex",
                                     CHAR(1),
                                     nullable=False,
                                     unique=False)
    
    cpf: Mapped[str] = mapped_column("cpf",
                                     CHAR(11),
                                     nullable=False,
                                     unique=True)

    zip: Mapped[str] = mapped_column("zip",
                                     CHAR(8),
                                     nullable=True,
                                     unique=False)

    street: Mapped[str] = mapped_column("street",
                                        VARCHAR(200),
                                        nullable=True,
                                        unique=False)

    street_number: Mapped[str] = mapped_column("street_number",
                                               INTEGER,
                                               nullable=True,
                                               unique=False)

    complement: Mapped[str] = mapped_column("complement",
                                            VARCHAR(200),
                                            nullable=True,
                                            unique=False)

    neighborhood: Mapped[str] = mapped_column("neighborhood",
                                              VARCHAR(200),
                                              nullable=True,
                                              unique=False)

    city: Mapped[str] = mapped_column("city",
                                      VARCHAR(200),
                                      nullable=True,
                                      unique=False)

    state: Mapped[str] = mapped_column("state",
                                       CHAR(2),
                                       nullable=True,
                                       unique=False)

    country: Mapped[str] = mapped_column("country",
                                         CHAR(3),
                                         nullable=True,
                                         unique=False)

    phone: Mapped[str] = mapped_column("phone",
                                       CHAR(11),
                                       nullable=False,
                                       unique=True)

    email: Mapped[str] = mapped_column("email",
                                       VARCHAR(50),
                                       nullable=False,
                                       unique=True)
