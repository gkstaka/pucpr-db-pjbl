from sqlalchemy import VARCHAR, FLOAT
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column

from models import Base


class Disorder(Base):
    __tablename__ = "disorder"

    id: Mapped[int] = mapped_column("id",
                                    MEDIUMINT,
                                    nullable=False,
                                    autoincrement=True,
                                    primary_key=True)

    name: Mapped[str] = mapped_column("name",
                                      VARCHAR(200),
                                      nullable=False,
                                      unique=True)

    category: Mapped[str] = mapped_column("category",
                                          VARCHAR(200),
                                          nullable=False,
                                          unique=False)

    symptoms: Mapped[str] = mapped_column("symptoms",
                                          VARCHAR(200),
                                          nullable=False,
                                          unique=False)

    risk_factors: Mapped[str] = mapped_column("risk_factors",
                                              VARCHAR(200),
                                              nullable=False,
                                              unique=False)

    prevalence: Mapped[str] = mapped_column("prevalence",
                                            FLOAT,
                                            nullable=False,
                                            unique=False)
