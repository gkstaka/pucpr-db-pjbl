from datetime import datetime

from sqlalchemy import DATETIME, ForeignKey, VARCHAR, INTEGER
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column

from models import Base, Patient, Psychologist, Treatment


class Therapy(Base):
    __tablename__ = "therapy"

    id: Mapped[int] = mapped_column("id",
                                    MEDIUMINT,
                                    nullable=False,
                                    autoincrement=True,
                                    primary_key=True)

    time: Mapped[str] = mapped_column("time",
                                      DATETIME,
                                      nullable=False,
                                      unique=False,
                                      default=datetime.now())

    purpose: Mapped[int] = mapped_column("purpose",
                                         VARCHAR(200),
                                         nullable=False,
                                         unique=True)

    capacity: Mapped[int] = mapped_column("capacity",
                                          INTEGER,
                                          nullable=False,
                                          unique=False)

    psychologist_id: Mapped[int] = mapped_column("psychologist_id",
                                                 MEDIUMINT,
                                                 ForeignKey(Psychologist.id),
                                                 nullable=False,
                                                 unique=False)
