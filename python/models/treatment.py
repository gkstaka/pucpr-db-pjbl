from datetime import datetime

from sqlalchemy import VARCHAR, DATETIME, ForeignKey
from sqlalchemy.dialects.mysql import MEDIUMINT
from sqlalchemy.orm import Mapped, mapped_column

from models import Base, Disorder, Patient


class Treatment(Base):
    __tablename__ = "treatment"

    id: Mapped[int] = mapped_column("id",
                                    MEDIUMINT,
                                    nullable=False,
                                    autoincrement=True,
                                    primary_key=True)

    name: Mapped[str] = mapped_column("name",
                                      VARCHAR(200),
                                      nullable=False,
                                      unique=False)

    start_date: Mapped[datetime] = mapped_column("start_date",
                                                 DATETIME,
                                                 nullable=False,
                                                 unique=False,
                                                 default=datetime.now())

    planned_end_date: Mapped[int] = mapped_column("planned_end_date",
                                                  DATETIME,
                                                  nullable=False,
                                                  unique=False,
                                                  default=datetime.now())


    patient_id: Mapped[int] = mapped_column("patient_id",
                                            MEDIUMINT,
                                            ForeignKey(Patient.id),
                                            nullable=False,
                                            unique=False)
