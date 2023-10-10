from datetime import datetime

from sqlalchemy import VARCHAR, DATETIME, ForeignKey
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column

from models import Base, Dosage


class Medicine(Base):
    __tablename__ = "medicine"

    id: Mapped[int] = mapped_column("id",
                                    MEDIUMINT,
                                    nullable=False,
                                    autoincrement=True,
                                    primary_key=True)

    name: Mapped[str] = mapped_column("name",
                                      VARCHAR(200),
                                      nullable=False,
                                      unique=True)

    composition: Mapped[str] = mapped_column("composition",
                                             VARCHAR(200),
                                             nullable=False,
                                             unique=True)

    usage_type: Mapped[int] = mapped_column("usage_type",
                                            VARCHAR(50),
                                            nullable=False,
                                            unique=False)

    indication: Mapped[str] = mapped_column("indication",
                                            VARCHAR(200),
                                            nullable=False,
                                            unique=False)

    contraindication: Mapped[str] = mapped_column("contraindication",
                                                  VARCHAR(200),
                                                  nullable=False,
                                                  unique=False)
